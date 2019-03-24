import pandas as pd

inv_col = ['ProductId']
inventory = pd.read_csv("../DataSets/inventory.csv", sep=";", names=inv_col, usecols=[0])
employeeWitem = pd.read_csv	("../DataSets/peoplewithitems.csv", sep=";", usecols=[0,3])

df = employeeWitem.groupby(employeeWitem.columns.tolist(), as_index=False).size()
print(df)
# df.to_csv("CountItemPerEmployee.csv", sep=';', encoding="utf-8")


