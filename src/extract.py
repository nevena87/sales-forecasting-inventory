import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

def load_sales_data(path: str = "data/sales.csv") -> pd.DataFrame:
    try:
        df = pd.read_csv(path)

        required_columns = ["date", "product_id", "quantity", "revenue"]
        for col in required_columns:
            if col not in df.columns:
                raise ValueError(f"Missing column in sales data: {col}")

        df["date"] = pd.to_datetime(df["date"])

        logging.info(f"Sales data loaded successfully: {df.shape}")
        return df

    except Exception as e:
        logging.error(f"Error loading sales data: {e}")
        raise


def load_inventory_data(path: str = "data/inventory.csv") -> pd.DataFrame:
    try:
        df = pd.read_csv(path)

        required_columns = ["product_id", "stock_quantity"]
        for col in required_columns:
            if col not in df.columns:
                raise ValueError(f"Missing column in inventory data: {col}")

        logging.info(f"Inventory data loaded successfully: {df.shape}")
        return df

    except Exception as e:
        logging.error(f"Error loading inventory data: {e}")
        raise


def load_all():
    sales = load_sales_data()
    inventory = load_inventory_data()

    if sales.empty or inventory.empty:
        raise ValueError("One of the datasets is empty")

    return sales, inventory