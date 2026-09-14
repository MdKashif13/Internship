import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('C:\\Users\\mdkas\\OneDrive\\Desktop\\INTERNSHIP\\Project 1\\ecommerce_orders_cleaned.csv')
#vectorized operations
est_day=df['Est_Delivery_Days'].to_numpy()
act_day=df['Actual_Delivery_Days'].to_numpy()
delivery_delay=act_day-est_day
df['Delivery_Delay']=delivery_delay

#Delivery Status
conditions=[
    df['Delivery_Delay'] < 0,
    df['Delivery_Delay'] == 0,
    (df['Delivery_Delay'])<0 & (df['Delivery_Delay'] <= 2),
    df['Delivery_Delay'] > 2
]
choices=['Early','On-Time','Minor Delay','Severe Delay']
df['Fulfillment_Status'] = np.select(conditions, choices, default='Unknown')

#percentile

perc = np.percentile(df["Order_Value"],95)
conditions = [
    df["Order_Value"] < perc,
    df["Order_Value"] > perc
]
choices = ['True', 'False']
df["High_Value_Order"] = np.select(conditions, choices, default='Same')


#vectorized operation for Net Revenue
df["Net_Revenue"] = df["Order_Value"]  * (1 - df["Discount_Percent"] / 100)
df.to_csv('C:\\Users\\mdkas\\OneDrive\\Desktop\\INTERNSHIP\\Project 1\\ecommerce_orders_numpy.csv', index=False)