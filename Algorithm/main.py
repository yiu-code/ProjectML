from Recommender import *
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import csr_matrix
countItems = pd.read_csv('./Count.csv', sep=";")
inventory = pd.read_csv('./DataSets/LaptopsV2.csv', sep=";")
employeeWitem = pd.read_csv("./DataSets/OrderHistoryV3.csv", sep=";")

# convert data to interger
inventory["ProductId"] = inventory["ProductId"].astype(np.int64)

countItems["UserId"] = countItems["UserId"].astype(np.int64)
countItems["ProductId"] = countItems["ProductId"].astype(np.int64)
countItems["Count"] = countItems["Count"].astype(np.int64)

employeeWitem["OrderId"] = employeeWitem["OrderId"].astype(np.int64)
employeeWitem["UserId"] = employeeWitem["UserId"].astype(np.int64)
employeeWitem["ProductId"] = employeeWitem["ProductId"].astype(np.int64)
employeeWitem.sort_values(by="OrderId")
     
def Main():
    recommmender = Recommender(inventory,countItems,employeeWitem, 12)
    product = recommmender.Knn()

    for i in product:
        print(i[0] +  " with a distance of: " + str(i[1]) )

# Office 1, 4, 8, 14, 20, 21, 26, 
# Developer 2, 5, 6, 9, 10, 11, 15, 19, 22, 24, 28, 30
# Designer 3, 7, 12, 13, 16, 17, 18, 23, 24, 27, 29    
#----------------------------------------------------------
# new Emplloyee with no history
#       Office 31, 38, 39
#       Developer  32, 34, 35, 36 
#       Designer 33, 37, 40
Main()