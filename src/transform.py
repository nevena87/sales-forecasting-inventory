import pandas as pd

def clean_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna()
    df['date'] = pd.to_datetime(df['date'])
    return df

def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    df['day'] = df['date'].dt.day
    df['month'] = df['date'].dt.month
    df['weekday'] = df['date'].dt.weekday
    return df

def aggregate_daily(df: pd.DataFrame) -> pd.DataFrame:
    agg = df.groupby(['date', 'product_id']).agg({
        'quantity': 'sum',
        'revenue': 'sum'
    }).reset_index()
    return agg