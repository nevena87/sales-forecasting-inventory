from extract import load_all
from transform import clean_sales_data, aggregate_daily
from model import SalesModel
from inventory import (
    calculate_daily_sales,
    compute_reorder_points,
    merge_with_inventory
)

def main():
    # 1. Extract
    sales, inventory = load_all()

    # 2. Transform
    sales = clean_sales_data(sales)
    sales = aggregate_daily(sales)

    # 3. Model
    model = SalesModel()
    model.train(sales)

    # koristi model za predikciju
    sales['predicted_revenue'] = model.predict(sales)

    # (opciono) pretvori revenue u quantity proxy
    sales['predicted_quantity'] = sales['predicted_revenue'] / (
        sales['revenue'] / sales['quantity']
    )

    # 4. Inventory (koristi predikcije!)
    pred_df = sales[['product_id', 'predicted_quantity']].copy()
    pred_df.rename(columns={'predicted_quantity': 'quantity'}, inplace=True)

    daily_sales = calculate_daily_sales(pred_df)

    reorder_df = compute_reorder_points(daily_sales)

    final_df = merge_with_inventory(inventory, reorder_df)

    # 5. Output
    print("\n=== PRODUCTS THAT NEED REORDER ===\n")
    print(final_df[final_df['need_reorder'] == True])

    print("\n=== FULL INVENTORY STATUS ===\n")
    print(final_df)


if __name__ == "__main__":
    main()