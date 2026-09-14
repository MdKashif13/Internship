import pandas as pd
import numpy as np

df=pd.read_csv('C:\\Users\\mdkas\\OneDrive\\Desktop\\INTERNSHIP\\Project 1\\ecommerce_orders_numpy.csv')

#Category Performance Analysis
category_summary = df.groupby("Category").agg(
    Total_Net_Revenue=("Net_Revenue", "sum"),
    Average_Discount=("Discount_Percent", "mean"),
    Rate_percentage=('Returned', lambda x: (x == 'Yes').mean() * 100)
)
print(category_summary.sort_values(by="Total_Net_Revenue", ascending=False))

df['Severe_Delay'] = df['Delivery_Delay'] > 3
fulfillment_summary=df.groupby("City_Tier")['Severe_Delay'].mean()*100
print(fulfillment_summary)

pivot_df = pd.pivot_table(
    data=df, 
    values='Customer_Rating',
    index='Category',     
    columns='Fulfillment_Status',   
    aggfunc='mean',              
)
print(pivot_df)

order_median =df["Order_Value"].median()

conditions=[
    (df['Discount_Percent'] >= 30) & (df["Returned"]=='Yes'),
    (df['Order_Value'] > order_median) & (df['Customer_Rating'] >= 4) & (df['Returned']=="No")
]
choices=['High-Risk Transaction', 'Loyal & Satisfied']
df['Customer_Segment']=np.select(conditions,choices,default='Standard Order')

df.to_csv('ecommerce_orders_final.csv', index=False)

