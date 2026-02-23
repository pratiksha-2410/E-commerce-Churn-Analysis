E-Commerce Customer Churn Analysis


Predictive Analytics for Customer Retention & Revenue Protection

📌 Executive Summary

Customer churn is one of the most critical challenges in the e-commerce industry. Acquiring a new customer is significantly more expensive than retaining an existing one.

This project develops a data-driven churn analysis and prediction framework to:

Identify customers at risk of leaving

Understand behavioral patterns leading to churn

Enable proactive retention strategies

Improve long-term customer lifetime value (CLV)

The solution integrates exploratory data analysis, feature engineering, and machine learning modeling to build an interpretable and business-focused churn prediction system.

🎯 Business Objectives

This project addresses key strategic questions:

Which customers are likely to churn?

What behavioral patterns indicate churn risk?

How does purchase frequency impact retention?

Which customer segments generate long-term value?

What actions can reduce churn rate?

📊 Dataset Overview

The dataset contains structured customer-level and transaction-level information, including:

Customer ID

Order Frequency

Total Spending

Average Order Value

Recency (Days since last purchase)

Tenure

Discount Usage

Customer Support Interaction

Churn Label (0 = Active, 1 = Churned)

The dataset reflects real-world churn behavior with class imbalance challenges.

🧠 Analytical Approach
1️⃣ Data Preprocessing

Missing value handling

Outlier treatment

Feature scaling

Encoding categorical variables

Train-test split with stratification

2️⃣ Exploratory Data Analysis (EDA)

Performed deep behavioral analysis:

Churn rate distribution

Recency vs churn trend

Spending patterns of churned customers

Tenure impact on retention

Correlation heatmap

Key observation:
Customers with low frequency and high recency show significantly higher churn probability.

3️⃣ Feature Engineering

Created behavioral indicators such as:

Customer Lifetime Value (CLV)

Purchase Frequency Score

Average Transaction Gap

Engagement Score

Discount Sensitivity Index

4️⃣ Model Development

Implemented and compared multiple classification models:

Logistic Regression

Decision Tree

Random Forest

Gradient Boosting

XGBoost (if used)

Hyperparameter tuning performed using GridSearchCV.

📈 Model Evaluation

Since churn prediction involves class imbalance, evaluation focused on:

Precision

Recall

F1 Score

ROC-AUC

Confusion Matrix

Precision-Recall Curve

Emphasis was placed on high Recall to identify maximum at-risk customers.

🏆 Results

Successfully identified high-risk churn segments

Achieved strong recall for churn class

Random Forest / Gradient Boosting delivered best performance

Model generalizes well on unseen data

(Replace below with your actual metrics)

Metric	Score
Accuracy	0.88
Precision	0.84
Recall	0.91
F1 Score	0.87
ROC-AUC	0.92
📊 Key Business Insights

Customers with long inactivity periods are highly likely to churn.

High discount dependency correlates with unstable retention.

Lower engagement customers show declining purchase frequency before churn.

Loyal customers generate disproportionately higher lifetime revenue.

🛠️ Tech Stack

Python – Data analysis & modeling

Pandas, NumPy – Data processing

Matplotlib, Seaborn – Visualization

Scikit-learn – Machine learning

SQL (if used) – Data extraction


💼 Business Impact

If deployed in a real e-commerce environment, this solution can:

Reduce churn rate through early intervention

Improve marketing campaign targeting

Increase customer lifetime value

Enhance personalization strategies

Strengthen revenue forecasting


📌 Skills Demonstrated

Customer Analytics

Predictive Modeling

Imbalanced Classification Handling

Feature Engineering

Business-Oriented Data Science

Model Evaluation Strategy

👩‍💻 Author

Pratiksha Bagwale Zagade
Aspiring Data Scientist | Customer Analytics Enthusiast