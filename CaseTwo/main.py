from Recommender import *
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import csr_matrix
countItems = pd.read_csv('./Count.csv', sep=";")
inventory = pd.read_csv('./DataSets/Laptops.csv')
employeeWitem = pd.read_csv	("./DataSets/OrderHistoryNew.csv", sep=";")

# convert data to interger
inventory["ProductId"] = inventory["ProductId"].astype(np.int64)

countItems["UserId"] = countItems["UserId"].astype(np.int64)
countItems["ProductId"] = countItems["ProductId"].astype(np.int64)
countItems["Count"] = countItems["Count"].astype(np.int64)

employeeWitem["OrderID"] = employeeWitem["OrderID"].astype(np.int64)
employeeWitem["UserId"] = employeeWitem["UserId"].astype(np.int64)
employeeWitem["ProductId"] = employeeWitem["ProductId"].astype(np.int64)
     
def Main():
    recommmender = Recommender(inventory,countItems,employeeWitem, 5)
    product = recommmender.Knn()

    for i in product:
        print(i)

Main()