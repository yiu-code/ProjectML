import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import csr_matrix

class Recommender:
    def __init__(self, inventory, countItems, employeeWitem, UserId ):
        self.inventory = inventory
        self.countItems = countItems
        self.employeeWitem = employeeWitem
        self.UserId = UserId
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

    def GetUserHistory(self):
        hist = []
        product = []
        for row in range (1, (len(self.employeeWitem))):
            if self.employeeWitem["UserId"][row] == self.UserId:
                hist.append(self.employeeWitem["OrderID"][row])
        hist.sort(reverse = True)
        del hist[5::] # only save the 5 most recent ID 

        #find each product Id for each 
        for i in hist:
            product.append(self.employeeWitem.at[i, "ProductId"])
        print(product)
        return product

    def Knn(self):
        # combine and drop the columns that is not needed for the algoritm
        combineItemCount = pd.merge(self.countItems, self.inventory, on="ProductId")
        dropColumns = ["Brand", "Image", "Price"] 
        combineItemCount = combineItemCount.drop(dropColumns, axis=1) 

        #drop NA
        combineItemCount = combineItemCount.dropna(axis = 0, subset = ['Title'])

        productAmountCount = (combineItemCount.groupby(by= ['Title'])['Count'].count().reset_index().rename(columns = {'Count': 'totalAmountCount'})[['Title', 'totalAmountCount']])
        
        #combine count data with total amount count data 
        countWithTotal = combineItemCount.merge(productAmountCount, left_on = "Title", right_on = 'Title', how= 'left')

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                #Take a look at this later
        #due to top 1 percent is a small amount of borrowed item we took the top 5-6% instead.
        # quantile = productAmountCount['totalAmountCount'].quantile(np.arange(.6, 1, .01)).mean()
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        CountpopluarItem = countWithTotal

        CountpopluarItem = CountpopluarItem.drop_duplicates(['UserId', 'Title'])
        CountpopluarItemPivot = CountpopluarItem.pivot(index = "ProductId", columns = 'UserId', values = 'Count').fillna(0)
        CountpopluarItemMaxtrix = csr_matrix(CountpopluarItemPivot.values)

        from sklearn.neighbors import NearestNeighbors

        model_knn = NearestNeighbors(metric= 'cosine', algorithm= 'brute')
        model_knn.fit(CountpopluarItemMaxtrix)

        queryIndex = self.GetUserHistory()
        ItemId = []
        for index in queryIndex:
            try:
                distances, indices = model_knn.kneighbors(CountpopluarItemPivot.iloc[int(index), :].values.reshape(1, -1), n_neighbors=3)
            except:
                # in case for new products and there is only 1 neighbour
                distances, indices = model_knn.kneighbors(CountpopluarItemPivot.iloc[int(index), :].values.reshape(1, -1), n_neighbors=2)
            
            for i in range(1, len(distances.flatten())):
                ItemId.append([indices.flatten()[i], distances.flatten()[i]])
        
        ItemId = sorted(ItemId, key= lambda x: x[1])
        recommendedTitles = []
        for i in ItemId:
            recommendedTitles.append(self.inventory.at[i[0], "Title"])

        # print(recommendedTitles)   
        # print(ItemId)
        return recommendedTitles