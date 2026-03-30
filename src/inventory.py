import pandas as pd

def calculate_daily_sales(df: pd.DataFrame):
    daily = df.groupby('product_id')['quantity'].mean().reset_index()
    daily.rename(columns={'quantity': 'daily_avg_sales'}, inplace=True)
    return daily

def compute_reorder_points(daily_sales: pd.DataFrame, safety_days=7):
    daily_sales['reorder_point'] = daily_sales['daily_avg_sales'] * safety_days
    return daily_sales

def merge_with_inventory(inventory_df: pd.DataFrame, reorder_df: pd.DataFrame):
    df = inventory_df.merge(reorder_df, on='product_id')
    df['need_reorder'] = df['stock_quantity'] < df['reorder_point']
    return df