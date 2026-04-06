import pandas as pd

def clean_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    # uklanjamo samo redove gde fale ključne vrednosti
    df = df.dropna(subset=["date", "product_id", "quantity"])

    # osiguravamo tipove
    df["date"] = pd.to_datetime(df["date"])
    df["product_id"] = df["product_id"].astype(int)
    df["quantity"] = df["quantity"].astype(float)
    df["revenue"] = df["revenue"].astype(float)

    return df

def aggregate_daily(df: pd.DataFrame) -> pd.DataFrame:
    df = (
        df.groupby(["date", "product_id"])
        .agg({
            "quantity": "sum",
            "revenue": "sum"
        })
        .reset_index()
    )

    return df

def merge_with_inventory(
    sales: pd.DataFrame,
    inventory: pd.DataFrame
) -> pd.DataFrame:

    df = pd.merge(sales, inventory, on="product_id", how="left")

    # ako nema stock info → postavi 0
    df["stock_quantity"] = df["stock_quantity"].fillna(0)

    return df

def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    # sortiranje (VAŽNO za time series)
    df = df.sort_values(["product_id", "date"])

    # vremenski feature-i
    df["day"] = df["date"].dt.day
    df["month"] = df["date"].dt.month
    df["weekday"] = df["date"].dt.weekday

    # lag feature (prodaja prethodnog dana)
    df["lag_1"] = df.groupby("product_id")["quantity"].shift(1)

    # rolling average (3 dana)
    df["rolling_mean_3"] = (
        df.groupby("product_id")["quantity"]
        .rolling(window=3)
        .mean()
        .reset_index(0, drop=True)
    )

    # uklanjamo NA (nastale zbog lag/rolling)
    df = df.dropna()

    return df