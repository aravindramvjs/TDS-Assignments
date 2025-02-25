import pandas as pd
import json
from rapidfuzz import process, fuzz
from metaphone import doublemetaphone  # For phonetic clustering

# Load the dataset
json_file = "./q-clean-up-sales-data.json"  # Replace with actual file path
with open(json_file, "r", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Ensure required columns exist
required_columns = {"city", "product", "sales"}
if not required_columns.issubset(df.columns):
    missing_columns = required_columns - set(df.columns)
    raise KeyError(f"Missing required columns: {missing_columns}")

# Convert sales column to numeric
df["sales"] = pd.to_numeric(df["sales"], errors="coerce")

# Step 1: Filter sales for "Bacon" with at least 63 units
filtered_df = df[(df["product"] == "Bacon") & (df["sales"] >= 63)]

# Step 2: Standardize City Names Using Phonetic Clustering
def get_phonetic_map(city_list):
    """Generate a phonetic mapping for city names based on double metaphone."""
    phonetic_map = {}
    for city in city_list:
        primary, alt = doublemetaphone(city)
        phonetic_key = primary or alt  # Use primary encoding if available
        phonetic_map[phonetic_key] = city
    return phonetic_map

# Define a reference list of correct city names
reference_cities = ["Manila", "Tokyo", "Mexico City", "London", "Jakarta", "Moscow", "Chennai", "Shanghai", "Lahore", "Karachi"]
phonetic_map = get_phonetic_map(reference_cities)

def normalize_city(city, phonetic_map):
    """Normalize city names using phonetic matching."""
    primary, alt = doublemetaphone(city)
    phonetic_key = primary or alt
    return phonetic_map.get(phonetic_key, city)  # Use the mapped city or keep original

# Apply normalization
filtered_df["city"] = filtered_df["city"].apply(lambda x: normalize_city(x, phonetic_map))

# Step 3: Aggregate Sales by City
sales_by_city = filtered_df.groupby("city")["sales"].sum().reset_index()

# Step 4: Extract Sales for Jakarta
jakarta_sales = sales_by_city[sales_by_city["city"] == "Jakarta"]["sales"].sum()

# Display Result
print(f"Total units of 'Bacon' sold in Jakarta (transactions ≥63 units): {jakarta_sales}")
