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

# Create Churn Label

rfm["Churn"] = np.where(rfm["Recency"] > 90,1,0)
print(rfm["Churn"])

# Total Loss

query = """SELECT SUM(Profit) AS Total_Loss
FROM orders
WHERE Profit < 0"""

Total_Loss = pd.read_sql(query,conn)

# Churn Customers

total_customers = rfm.shape[0]
churn_customers = rfm['Churn'].sum()

churn_rate = churn_customers / total_customers * 100

print("Total Customers:", total_customers)
print("Churn Customers:", churn_customers)
print("Churn Rate: {:.2f}%".format(churn_rate))

# Visualization

# Churn Distribution

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(6,4))
sns.countplot(x='Churn',data=rfm)
plt.title("Churn Distribution")
plt.xlabel("Churn(0=no,1=yes)")
plt.ylabel("Number of Customers")
plt.show()

# Churn Rate Percentage Pie Chart

churn_counts = rfm['Churn'].value_counts()

plt.figure(figsize=(6,6))
plt.pie(churn_counts, 
        labels=['Not Churned', 'Churned'],
        autopct='%1.1f%%',
        startangle=90)
plt.title("Churn Percentage")
plt.show()

# Recency VS Churn

plt.figure(figsize=(6,4))
sns.boxplot(x='Churn', y='Recency', data=rfm)
plt.title("Recency vs Churn")
plt.show()

# Frequency VS Churn 
plt.figure(figsize=(6,4))
sns.boxplot(x='Churn', y='Frequency', data=rfm)
plt.title("Frequency vs Churn")
plt.show()

# Monetary VS Churn

plt.figure(figsize=(6,4))
sns.boxplot(x='Churn', y='Monetary', data=rfm)
plt.title("Monetary vs Churn")
plt.show()


