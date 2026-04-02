from extract import load_all
from transform import clean_sales_data, aggregate_daily
from model import SalesModel
from inventory import calculate_daily_sales, compute_reorder_points, merge_with_inventory


def main():
    # 1. Extract
    sales, inventory = load_all()

    # 2. Transform (minimal cleaning only)
    sales = clean_sales_data(sales)

    # ⚠️ više ne radiš feature_engineering ovde

    # 3. Model
    model = SalesModel()
    model.train(sales)

    predictions = model.predict(sales)

    sales['predicted_revenue'] = predictions

    # 4. Inventory logic
    daily_sales = calculate_daily_sales(sales)
    reorder_df = compute_reorder_points(daily_sales)

    final_df = merge_with_inventory(inventory, reorder_df)

    # 5. Output
    print("\n=== PRODUCTS THAT NEED REORDER ===\n")
    print(final_df[final_df['need_reorder'] == True])


if __name__ == "__main__":
    main()