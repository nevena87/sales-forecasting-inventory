import pandas as pd

def load_sales_data(path="data/sales.csv"):
    df = pd.read_csv(path)
    return df

def load_inventory_data(path="data/inventory.csv"):
    df = pd.read_csv(path)
    return df

def load_all():
    sales = load_sales_data()
    inventory = load_inventory_data()
    return sales, inventory