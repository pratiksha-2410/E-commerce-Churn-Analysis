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

query = ("""
SELECT Customer_ID,
MAX(Order_Date) AS Last_Order,
COUNT(Order_ID) AS Frequency,
SUM(Sales) AS Monetary
FROM orders
GROUP BY Customer_ID
""")

rfm = pd.read_sql(query,conn)
print(rfm)

rfm["Last_Order"] = pd.to_datetime(rfm["Last_Order"])
Latest_Order = rfm["Last_Order"].max()
rfm["Recency"] = (Latest_Order - rfm["Last_Order"]).dt.days

print("\n",rfm[["Customer_ID","Recency"]].to_string(index=True))

# Calculating Frequency

query = """SELECT Customer_ID,
COUNT(Order_ID) AS Frequency
FROM orders
GROUP BY Customer_ID"""

rfmF = pd.read_sql(query,conn)
rfmf = rfm["Frequency"]

print(rfm[["Customer_ID","Frequency"]].to_string(index=False))

# Calculating Monetary

query = """SELECT Customer_ID,
SUM(Sales) AS Monetary
FROM orders
GROUP BY Customer_ID"""

rfmM = pd.read_sql(query,conn)
rfmM = rfm["Monetary"]
print(rfm[["Customer_ID","Monetary"]].to_string(index=False))


