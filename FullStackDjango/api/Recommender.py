import numpy as np
import pandas as pd
from .models import Order, ProductList, Product, User
from scipy.sparse import csr_matrix
from django.db import connection
import itertools
import random

class Recommender:
    def __init__(self, UserId):
        self.inventory = pd.DataFrame(list(Product.objects.all().values()))
        self.inventory.index += 1
        
        self.employeeList = pd.DataFrame(list(User.objects.all().values()))
        self.employeeList.index += 1 

        self.fetchCount = connection.cursor().execute("SELECT u.id, pl.product_id, SUM(pl.amount) FROM api_user AS u JOIN api_order AS o ON u.id = o.user_id JOIN api_productlist AS pl ON o.id = pl.order_id GROUP BY u.id, pl.product_id")
        self.count = pd.DataFrame(list(self.fetchCount.fetchall()))
        self.count.index += 1
        # self.count[1] is all UserID;      self.count[2] is all productId;       self.count[3]  is count per product


        #self.employeeWitem = employeeWitem
        #self.employeeWitem.index += 1 
        #self.UserId = UserId


        #self.countItems = countItems
        #self.DataFiltering()
        print(self.count[0][0])