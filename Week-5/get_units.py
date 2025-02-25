import json

# Load JSON file
json_file = "q-clean-up-sales-data.json"  # Change this to the actual file path

# Load data
with open(json_file, "r", encoding="utf-8") as f:
    sales_data = json.load(f)

# Step 1: Filter transactions
total_units = 0

for entry in sales_data:
    city = entry.get("city", "").strip()
    product = entry.get("product", "").strip().lower()
    sales = entry.get("sales", 0)  # Using "sales" instead of "units_sold"

    # Convert sales to integer if it's a string
    try:
        sales = int(sales)
    except ValueError:
        sales = 0

    # Apply filters: City must be Jakarta, Product must be Bacon, and sales >= 63
    if city.lower() == "jakarta" and product == "bacon" and sales >= 63:
        total_units += sales

# Print final result
print(f"Total units of Bacon sold in Jakarta on transactions with at least 63 units: {total_units}")
