import json

def extract_sales_from_jsonl(file_path):
    total_sales = 0
    with open(file_path, 'r') as file:
        for line in file:
            try:
                # Attempt to load JSON; ignore lines that fail due to truncation
                entry = json.loads(line)
                # Add sales value if present and valid
                if 'sales' in entry and isinstance(entry['sales'], (int, float)):
                    total_sales += entry['sales']
            except json.JSONDecodeError:
                # Skip lines that can't be parsed
                continue
    return total_sales
# Calculate total sales
total_sales = extract_sales_from_jsonl("./q-parse-partial-json.jsonl")
print(total_sales)
