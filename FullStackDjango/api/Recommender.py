"""
First all the needed methods are imported:
Pandas is a data structure and analysis tool supporting data analysis workflow. 
Numpy supports the mathematical calculations that must be done. 
Mathplotlib has the ability to portray the data in graphs. 
SciPy is a package that optimalizes linear algebra and statistics. 
Itertools is used for efficient looping through data.
Random is used to generate random numbers.
"""
import numpy as np
import pandas as pd
from .models import Order, ProductList, Product, User
from scipy.sparse import csr_matrix
from django.db import connection
import itertools
import random


"""
The class Recommender is created. A class is a set of objects having
some attributes in common. It is a blueprint for individual objects
with exact behaviour. __init__ is known as a constructor. This method
is called  when an object is created from the class and it allows the
class to initialize the attributes of a class. In the def __init__
UserId is made global and data received from the database is converted
to be able to use it for the algoritm and to make it compatible with
the rest of the website.
- self.count[0] is all UserID
- self.count[1] is all productId
- self.count[2]  is count per product
"""

class Recommender:
    def __init__(self, UserId):
        self.UserId = UserId    
        self.inventory = pd.DataFrame(list(Product.objects.all().values()))
        self.inventory.index += 1        
        self.employeeList = pd.DataFrame(list(User.objects.all().values()))
        self.employeeList.index += 1 
        self.fetchCount = connection.cursor().execute("SELECT u.id, pl.product_id, SUM(pl.amount) FROM api_user AS u JOIN api_order AS o ON u.id = o.user_id JOIN api_productlist AS pl ON o.id = pl.order_id GROUP BY u.id, pl.product_id")
        self.countItems = pd.DataFrame(list(self.fetchCount.fetchall()))
        self.countItems.index += 1
        self.fetchEmployeeWithItem = connection.cursor().execute("SELECT o.id, o.user_id, pl.product_id, pl.amount FROM api_order AS o JOIN api_productlist AS pl ON o.id = pl.order_id ORDER BY o.id, o.user_id, pl.product_id;")
        self.employeeWithItem = pd.DataFrame(list(self.fetchEmployeeWithItem.fetchall()))
        self.employeeWithItem.index += 1
        self.DataFiltering()

        #Received an AttributeError. 'Recommender' object has no attribute 'count' :c
        #print(self.count[0][1])      # test

    """
    A value called newCount is made. It consists of the global variable
    countItems. countItems is the converted data from the database which
    shows the userID and the productID of the borrowed product + the 
    total amount of the referring product that has been borrowed. The new
    self.countItems filters out products which have been borrowed <2.
    """
    def DataFiltering(self):
        newCount = self.countItems["Count"].value_counts()
        self.countItems = self.countItems[self.countItems["Count"].isin(newCount[newCount < newCount[1]].index)]
      

    """
    GetTopBorrowedItems is a simple groupby function to get the top borrowed
    items from the database. totalCountPerItem adds the amount of times an 
    item has been borrowed. toprecommendedItems merges the results of the
    totalCountPerItem with the inventory
    """
    def GetTopBorrowedItems(self, num):
        totalCountPerItem = pd.DataFrame(self.countItems.groupby(['ProductId'])['Count'].count())  # pd.DataFrame kan weggelaten worden?
        toprecommendedItems = pd.merge(totalCountPerItem.sort_values("Count", ascending=False), self.inventory, on="ProductId")
        return toprecommendedItems.head(num)


    """
    CheckAndGetHistory will first call the CreateUserHistoryArray to get an
    array based on the user's history. If the history appears to be empty
    (with other words, when a new user wants to make use of the system),
    a related recommandation based on the new user's function within the 
    company will show. This is done based on the history of a random
    user with the same function. After the for-loop the fuction
    CreateUserHistory is called, but this time with a random employee ID. In
    the end, the function returns an array with productID's (NOT oderID's).
    """
    def CheckAndGetHistory(self):
        hist = self.CreateUserHistoryArray(self.UserId)
        print("history of current user:")
        if len(hist) == 0:
            userIdArray = []
            jobTitle = self.employeeList.loc[(self.UserId), "jobtitle"]
            print(jobTitle)          
            sameFunction = self.employeeList['UserId'].where(self.employeeList['jobtitle'] == jobTitle).dropna()
            for i in sameFunction:
                if int(i) <= 30:
                    userIdArray.append(int(i))
            randomId = random.choice(userIdArray)
            print("history from random user")
            hist = self.CreateUserHistoryArray(randomId)
        print("previous borrowed items:")
        print(hist)
        return hist


    """
    In the CreateUserHistoryArray functon, two empty lists are made. One for
    the history of the OrderId and one of the products, filled with the 
    ItemId's. The first for-loop loops through all the previously made
    orders and adds the order to the hist list if the UserId of the user
    that has made the order, matches the UserId of the current user. After
    all the orders are added, the order of the list is reversed so that the
    most 'recent' order is on top of the list. The second for-loop adds all
    the ProductId's of all the matching orders to the product list. After that
    all the duplicates are dropped. After that only the five most recent items
    are shown.
    """
    def CreateUserHistoryArray(self, Id):
        hist = []
        product = []
        for row in range (1, (len(self.employeeWitem))):
            if self.employeeWitem["UserId"][row] == Id:
                hist.append(self.employeeWitem["OrderId"][row])
        hist.sort(reverse = True)
        for i in hist:
            product.append(self.employeeWitem.at[(i), "ProductId"])
        product = list(dict.fromkeys(product)) 
        if len(product) > 5:
            del product[5::] 
        return product


    """
    The algorithm starts with combining columns that are needed for the
    algorithm and dropping the ones that are not needed. For instance the
    count data, together with the data of the total amount count, they are
    combined. Based on the adjusted data, a matrix is formed. After importing 
    NearestNeigbours from sklearn.neighbors, a knn model is created. This is 
    filled with the matrix. queryIndex will go to the global function
    CheckAndGetHistory to get an array filled with relevant items. 
    
    The first for-loop loops through the array to get the distances. Within
    the loop is a try except just in case new products would be added to the
    database and there is only one neighbor. Each of the distances are then 
    added to the previously empty list ItemId. Afterwards, a new empty list
    called idList is made fot the second for-loop. The second for loop loops
    through the items in the ItemId list and adds one to the index due to the
    index starting at 0 and the products starting at 1. The value of the array
    is obviously used to find the ID of the products in the database.

    IMPORTANT NOTES - Take a look at this later:
    In pandas the index starts at 0. Unlike SQL, where the index starts at 1. 
    Since we need to look up items in the inventory, employewithitem and
    employeelist, it will make the job easier by setting the index at 1, 
    so we don't have to add 1 the whole time while writing code.

    Due to the top 1 percent being a small amount borrowed items, we took the top 5-6% instead.
    quantile = productAmountCount['totalAmountCount'].quantile(np.arange(.9, 1, .01)).mean()
    print(quantile)

    """
    def Knn(self):
        combineItemCount = pd.merge(self.countItems, self.inventory, on="ProductId")
        dropColumns = ["Brand", "Image", "Price", "Category"] 
        combineItemCount = combineItemCount.drop(dropColumns, axis=1) 
        combineItemCount = combineItemCount.dropna(axis = 0, subset = ['Title'])
        productAmountCount = (combineItemCount.groupby(by= ['Title'])['Count'].sum().reset_index().rename(columns = {'Count': 'totalAmountCount'})[['Title', 'totalAmountCount']])
        countWithTotal = combineItemCount.merge(productAmountCount, left_on = "Title", right_on = 'Title', how= 'left')
        CountpopluarItem = countWithTotal
        CountpopluarItem = CountpopluarItem.drop_duplicates(['UserId', 'Title'])
        CountpopluarItemPivot = CountpopluarItem.pivot(index = "ProductId", columns = 'UserId', values = 'Count').fillna(0)
        CountpopluarItemMaxtrix = csr_matrix(CountpopluarItemPivot.values)

        from sklearn.neighbors import NearestNeighbors

        model_knn = NearestNeighbors(metric= 'cosine', algorithm= 'brute')
        model_knn.fit(CountpopluarItemMaxtrix)
        queryIndex = self.CheckAndGetHistory()
        ItemId = []

        for index in queryIndex:
            try:
                distances, indices = model_knn.kneighbors(CountpopluarItemPivot.loc[int(index), :].values.reshape(1, -1), n_neighbors=3)
            except:
                distances, indices = model_knn.kneighbors(CountpopluarItemPivot.loc[int(index), :].values.reshape(1, -1), n_neighbors=2)
            for i in range(1, len(distances.flatten())):
                ItemId.append([indices.flatten()[i], distances.flatten()[i]])
        ItemId = sorted(ItemId, key= lambda x: x[1])
        print(ItemId)
        idList = []

        for item in ItemId:
            idList.append((item[0] + 1))
        idList = list(dict.fromkeys(idList))  
        print("for web application no duplicate ID:")
        print(idList)
        # Needed this return for web application to give an array of product Id and find them in the DB
        # return idList


        #extra for testing in console so it returns a array with name and distance. 
        #for testing the index does not have to increase with one because the tabel with products in datafram starts with 0 instead of 1
        print("---------------------------------------------")
        print("test log for console with duplicates and distance")
        recommendedTitles = []
        index = 0
        while index < len(ItemId):
            recommendedTitles.append([self.inventory.at[ItemId[index][0], "Title"], ItemId[index][1]])
            index = index + 1
        return recommendedTitles
