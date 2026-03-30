📊 Sales Forecasting & Inventory Optimization System
📌 Project Overview

This project demonstrates an end-to-end data analytics pipeline for sales analysis, demand forecasting, and inventory optimization.

The system helps businesses:

Understand sales performance
Predict future demand
Optimize inventory levels
Reduce stock-outs and overstock situations
🎯 Objectives
Analyze historical sales data
Build a forecasting model for future sales
Identify products at risk of stock-out
Generate reorder recommendations
Visualize insights through a dashboard
🧰 Tech Stack
Python (pandas, numpy, scikit-learn, statsmodels)
SQL (data analysis & joins)
Power BI (dashboard & visualization)
CSV files (data source)
Git (version control)
🏗️ Project Structure
project/
│
├── data/
│   ├── sales.csv
│   ├── inventory.csv
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── model.py
│   ├── inventory.py
│   ├── main.py
│
├── dashboard/
│   ├── dashboard.pbix
│
└── README.md
🔄 Pipeline Workflow
1. Extract
Load sales and inventory data from CSV files
2. Transform
Data cleaning
Date formatting
Feature engineering
3. Model
Train a regression model to predict revenue
Generate sales forecasts
4. Inventory Optimization
Calculate average daily sales
Define reorder points
Identify products that need restocking
5. Output
Generate actionable inventory recommendations
▶️ How to Run the Project
# 1. Navigate to project folder
cd project

# 2. Run the pipeline
python src/main.py
📊 Example Output
=== PRODUCTS THAT NEED REORDER ===

product_id | stock_quantity | reorder_point | need_reorder
---------------------------------------------------------
104        | 15             | 28            | True
109        | 5              | 21            | True
📈 Dashboard (Power BI)

The dashboard includes:

KPI Metrics
Total Revenue
Total Quantity Sold
Average Daily Sales
Visualizations
📈 Sales trend over time (Line chart)
📊 Top products (Bar chart)
📦 Stock levels (Bar chart)
⚠️ Reorder list (Table)
🧠 Key Features
End-to-end pipeline (ETL + ML + business logic)
Sales forecasting model
Inventory optimization logic
SQL-based analysis
Business-oriented insights
Interactive dashboard
💼 Business Value

This solution enables:

Reduced stock-outs
Prevention of overstocking
Improved demand planning
Data-driven decision making
🚀 Future Improvements
Implement advanced forecasting models (ARIMA, Prophet, LSTM)
Automate pipeline using Airflow
Connect to a real database (PostgreSQL/MySQL)
Deploy as an API or dashboard application
👩‍💻 Author

Nevena Ćulibrk
