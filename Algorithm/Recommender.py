import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import csr_matrix
import itertools
import random

class Recommender:
    def __init__(self, inventory, countItems, employeeWitem, UserId, employeeList):
        self.inventory = inventory
        self.countItems = countItems
        self.employeeWitem = employeeWitem
        self.UserId = UserId
        self.employeeList = employeeList
        self.DataFiltering()

    #simpel groupby function to get top borrowed Items
    def GetTopBorrowedItems(self, num):
        #count x amount time that a item have been borrowed
        totalCountPerItem = pd.DataFrame(self.countItems.groupby(['ProductId'])['Count'].count())

        #merge total count Per Item with inventory 
        toprecommendedItems = pd.merge(totalCountPerItem.sort_values("Count", ascending=False), self.inventory, on="ProductId")

        return toprecommendedItems.head(num)

    def DataFiltering(self):
        newCount = self.countItems["Count"].value_counts()
        # filter out products with borrow rate < 2
        self.countItems = self.countItems[self.countItems["Count"].isin(newCount[newCount < newCount[1]].index)]

    def CheckUserHistory(self, UserId):
        hist = []
        product = []
        userIdArray = []
        print(self.UserId)
        for row in range (1, (len(self.employeeWitem))):
            if self.employeeWitem["UserId"][row] == UserId:
                hist.append(self.employeeWitem["OrderId"][row])
                #print("Item added")
        hist.sort(reverse = True)

        if len(hist) == 0:
            changeToDifferentUser = ChangeUsers(self.UserId)
            return changeToDifferentUser
            

        else:
            print("list is empty")
            del hist[5::] # only save the 5 most recent ID 
            for i in hist:
                product.append(self.employeeWitem.at[(i-1), "ProductId"])
            print(product)
            return product
        
    def ChangeUsers(self, UserId):
        test = 1
        return CheckUserHistory(test)



    # def GetUserHistory(self, UserId):
    #     hist = []
    #     product = []
    #     userIdArray = []
    #     print(self.UserId)
    #     for row in range (1, (len(self.employeeWitem))):
    #         if self.employeeWitem["UserId"][row] == UserId:
    #             hist.append(self.employeeWitem["OrderId"][row])
    #             #print("Item added")
    #     hist.sort(reverse = True)

    #     if len(hist) == 0:
    #         self.GetUserHistory(self.ChangeUser())
    #         print("User has no order history")
    #         print(self.UserId)
            
            

    #     if len(hist) > 5:
            # del hist[5::] # only save the 5 most recent ID 
            # for i in hist:
            #     product.append(self.employeeWitem.at[(i-1), "ProductId"])
            # print(product)
            # return product
        

    # def ChangeUser(self):
    #     employeeList["UserId"] = employeeList["UserId"].astype(np.int64)
    #     randomUser = random.choice(employeeList["UserId"])
    #     print (randomUser)
    #     return randomUser


            # print(hist)
            # for i in hist:
            #     product.append(self.employeeWitem.at[(i-1), "ProductId"])
            # print(product)
            # return product


            
# WAARSCHIJNLIJK ZITTEN ER VEEL TYFUSFOUTEN IN MAAR DAT KAN ME NU HELEMAAL NIKS BOEIEN
            
        # als len(hist) < 5:

        #
        #   haal user history van alle jobtitles binnen 

        #   print user history lijst

        #   uit alle resultaten
        #   randomizer voor 5 producten

        #   print resultaten randomizer


        #find each product Id for each 
        # print(hist)
        # for i in hist:
        #     product.append(self.employeeWitem.at[(i-1), "ProductId"])
        # print(product)
        # return product

    def Knn(self):
        # combine and drop the columns that is not needed for the algoritm
        combineItemCount = pd.merge(self.countItems, self.inventory, on="ProductId")
        dropColumns = ["Brand", "Image", "Price", "Category"] 
        combineItemCount = combineItemCount.drop(dropColumns, axis=1) 

        #drop NA
        combineItemCount = combineItemCount.dropna(axis = 0, subset = ['Title'])

        productAmountCount = (combineItemCount.groupby(by= ['Title'])['Count'].sum().reset_index().rename(columns = {'Count': 'totalAmountCount'})[['Title', 'totalAmountCount']])
   
        
        #combine count data with total amount count data 
        countWithTotal = combineItemCount.merge(productAmountCount, left_on = "Title", right_on = 'Title', how= 'left')
        # print(countWithTotal)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                #Take a look at this later
        #due to top 1 percent is a small amount of borrowed item we took the top 5-6% instead.
        # quantile = productAmountCount['totalAmountCount'].quantile(np.arange(.9, 1, .01)).mean()
        # print(quantile)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        CountpopluarItem = countWithTotal

        CountpopluarItem = CountpopluarItem.drop_duplicates(['UserId', 'Title'])
        CountpopluarItemPivot = CountpopluarItem.pivot(index = "ProductId", columns = 'UserId', values = 'Count').fillna(0)
        CountpopluarItemMaxtrix = csr_matrix(CountpopluarItemPivot.values)

        from sklearn.neighbors import NearestNeighbors

        model_knn = NearestNeighbors(metric= 'cosine', algorithm= 'brute')
        model_knn.fit(CountpopluarItemMaxtrix)

        queryIndex = self.CheckUserHistory(self.UserId)
        ItemId = []
        for index in queryIndex:
            try:
                distances, indices = model_knn.kneighbors(CountpopluarItemPivot.loc[int(index), :].values.reshape(1, -1), n_neighbors=3)
            except:
                # in case for new products and there is only 1 neighbour
                distances, indices = model_knn.kneighbors(CountpopluarItemPivot.loc[int(index), :].values.reshape(1, -1), n_neighbors=2)
            
            for i in range(1, len(distances.flatten())):
                ItemId.append([indices.flatten()[i], distances.flatten()[i]])
        
        ItemId = sorted(ItemId, key= lambda x: x[1])
        
        print(ItemId)
        idList = []
        # plus one because of index start at 0 and product start at 1.
        #value from the array is to use to find the ID in DB 
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