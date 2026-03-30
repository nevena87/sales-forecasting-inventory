# 📊 Sales Forecasting & Inventory Optimization System

## 📌 Project Overview

This project demonstrates an end-to-end data analytics pipeline for **sales analysis, demand forecasting, and inventory optimization**.

The goal is to help businesses:
- Understand sales performance
- Predict future demand
- Optimize inventory levels
- Reduce stock-outs and overstock situations

---

## 🎯 Objectives

- Analyze historical sales data
- Build a forecasting model for future sales
- Identify products at risk of stock-out
- Generate reorder recommendations
- Visualize insights through a dashboard

---

## 🧰 Tech Stack

- **Python** (pandas, numpy, scikit-learn, statsmodels)
- **SQL** (data analysis & joins)
- **Power BI** (dashboard & visualization)
- **CSV files** (data source)
- **Git** (version control)



## 🏗️ Project Structure
project/
│
├── data/
│   ├── sales.csv
│   └── inventory.csv
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── model.py
│   ├── inventory.py
│   └── main.py
│
├── dashboard/
│   └── dashboard.pbix
│
└── README.md


## 🔄 Pipeline Workflow

1. **Extract**
   - Load sales and inventory data from CSV files

2. **Transform**
   - Clean data
   - Convert date formats
   - Perform feature engineering

3. **Model**
   - Train a regression model to predict revenue
   - Generate sales forecasts

4. **Inventory Optimization**
   - Calculate average daily sales
   - Define reorder points
   - Identify products needing restock

5. **Output**
   - Generate recommendations for inventory replenishment

---

## ▶️ How to Run the Project

### 1. Navigate to project folder
cd project

### 2. Run the pipeline
python src/main.py

## 📊 Example Output

### Products That Need Reorder

| product_id | stock_quantity | reorder_point | need_reorder |
|------------|---------------|---------------|--------------|
| 104        | 15            | 28            | True         |
| 109        | 5             | 21            | True         |

## 📈 Dashboard (Power BI)

The dashboard includes:

KPI Metrics:
Total Revenue
Total Quantity Sold
Average Daily Sales

Visualizations:
📈 Sales trend over time (Line chart)
📊 Top products (Bar chart)
📦 Stock levels (Bar chart)
⚠️ Reorder list (Table)

## 🧠 Key Features
End-to-end data pipeline (ETL + ML + business logic)
Sales forecasting model
Inventory optimization logic
SQL-based analysis
Business-oriented insights
Dashboard visualization

## 💼 Business Value
This solution helps:
Reduce stock-outs
Avoid overstocking
Improve demand planning
Enable data-driven decision making

## 🚀 Future Improvements
Implement advanced forecasting models (ARIMA, Prophet, LSTM)
Automate pipeline using Airflow
Connect to real database (PostgreSQL/MySQL)
Deploy as API or dashboard app

## 👩‍💻 Author
Nevena Ćulibrk
