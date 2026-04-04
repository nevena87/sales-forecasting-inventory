import pandas as pd

# ---------------------------
# Calculate daily average sales
# ---------------------------
def calculate_daily_sales(df: pd.DataFrame) -> pd.DataFrame:
    daily = (
        df.groupby('product_id')['quantity']
        .mean()
        .reset_index()
    )

    daily.rename(columns={'quantity': 'daily_avg_sales'}, inplace=True)

    return daily


# ---------------------------
# Compute reorder point
# ---------------------------
def compute_reorder_points(
    daily_sales: pd.DataFrame,
    lead_time: int = 5,
    safety_stock: int = 10
) -> pd.DataFrame:

    daily_sales['reorder_point'] = (
        daily_sales['daily_avg_sales'] * lead_time
        + safety_stock
    )

    return daily_sales


# ---------------------------
# Merge with inventory & decision
# ---------------------------
def merge_with_inventory(
    inventory_df: pd.DataFrame,
    reorder_df: pd.DataFrame
) -> pd.DataFrame:

    df = inventory_df.merge(reorder_df, on='product_id', how='left')

    # ako nema podataka o prodaji → postavi 0
    df['daily_avg_sales'] = df['daily_avg_sales'].fillna(0)
    df['reorder_point'] = df['reorder_point'].fillna(0)

    # odluka
    df['need_reorder'] = df['stock_quantity'] < df['reorder_point']

    # koliko naručiti (AKO treba)
    df['order_quantity'] = (
        df['reorder_point'] - df['stock_quantity']
    ).clip(lower=0)

    return df