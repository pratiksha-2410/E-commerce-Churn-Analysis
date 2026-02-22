# Import Labraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# Create Database Connection
conn = sqlite3.connect("Customer_Churn.db")
cursor = conn.cursor()

# Load Dataset

df = pd.read_csv("ecommerce_customer_churn_dataset.csv")
df.to_sql("orders",conn,if_exists="append",index=False)
print(df.head(10))

# Data Featuring

print("shape:",df.shape)
print()
print("size:",df.size)
print()
print("info:",df.info)
print()
print("describe:",df.describe)

# Data Cleaning

# missisng values
print("\n Missing Values:",df.isna().sum())
# duplicated values
print("\n Duplicate Value:",df.duplicated().sum())
# Convert Dates
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# RFM Analysis (Recency,Frequency,Monetary)

# Extract Month
df["Month"] = df["Order_Date"].dt.month
# Extract Year
df["Year"] = df["Order_Date"].dt.year
# Calculate RFM 

from datetime import datetime 
today = datetime.now()

rfm = df.groupby('Customer_ID').agg({
    'Order_Date': lambda x: (today - x.max()).days,
    'Order_ID': 'count',
    'Sales': 'sum'
})

rfm.columns = ['Recency', 'Frequency', 'Monetary']

print(rfm)