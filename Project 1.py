import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv('C:\\Users\\mdkas\\OneDrive\\Desktop\\INTERNSHIP\\Project 1\\ecommerce_orders.csv', encoding='latin-1')

'''df.info()
print(df.shape)
print(df.dtypes)
print(df.isnull().sum())'''
#print(df.duplicated())

#remove duplicate
df.drop_duplicates(keep='first', inplace=True)
#upper case
df["Payment_Method"] = df["Payment_Method"].str.upper().str.strip()
# groupby category and fill missing values with median
df["Order_Value"] = df.groupby('Category')['Order_Value'].transform('median')
#customer_rating filling missing values with mode
df['Customer_Rating'].fillna(df['Customer_Rating'].mode()[0], inplace=True)
df.to_csv('C:\\Users\\mdkas\\OneDrive\\Desktop\\INTERNSHIP\\Project 1\\ecommerce_orders_cleaned.csv', index=False)
