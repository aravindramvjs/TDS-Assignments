import pandas as pd
from datetime import datetime

def clean_and_calculate_margin(file_path):
    # Load the Excel file
    df = pd.read_excel(file_path)
    
    # Trim and normalize strings in Customer Name and Country
    df['Customer Name'] = df['Customer Name'].str.strip()
    df['Country'] = df['Country'].str.strip().str.upper()
    
    # Standardize country names (Example: mapping 'USA', 'U.S.A', 'US' to 'USA')
    country_map = {'USA': 'USA', 'U.S.A': 'USA', 'US': 'USA', 'INDIA': 'IN', 'IND': 'IN'}
    df['Country'] = df['Country'].replace(country_map)
    
    # Standardize Date Formats
    def parse_date(date):
        for fmt in ("%m-%d-%Y", "%Y/%m/%d", "%Y-%m-%d"):
            try:
                return datetime.strptime(str(date), fmt)
            except ValueError:
                continue
        return pd.NaT  # Return Not a Time if the format is unknown
    
    df['Date'] = df['Date'].apply(parse_date)
    df = df.dropna(subset=['Date'])
    
    # Extract Product Name before the slash
    df['Product'] = df['Product/Code'].str.split('/').str[0].str.strip()
    
    # Clean and Convert Sales and Cost fields
    df['Sales'] = df['Sales'].astype(str).str.replace('USD', '').str.strip().astype(float)
    df['Cost'] = df['Cost'].astype(str).str.replace('USD', '').str.strip()
    df['Cost'] = pd.to_numeric(df['Cost'], errors='coerce')
    df['Cost'].fillna(df['Sales'] * 0.5, inplace=True)  # Assign 50% of Sales if Cost is missing
    
    # Apply Filters
    filter_date = datetime(2022, 12, 21, 22, 5, 36)
    df_filtered = df[(df['Date'] <= filter_date) & (df['Product'] == 'Eta') & (df['Country'] == 'IN')]
    
    # Calculate Total Sales, Total Cost, and Total Margin
    total_sales = df_filtered['Sales'].sum()
    total_cost = df_filtered['Cost'].sum()
    total_margin = (total_sales - total_cost) / total_sales if total_sales != 0 else 0
    
    return total_margin

# Example usage
file_path = "q-clean-up-excel-sales-data.xlsx"
total_margin = clean_and_calculate_margin(file_path)
print(f"Total Margin: {total_margin:.2%}")