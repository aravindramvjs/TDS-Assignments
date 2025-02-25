import json

def calculate_total_sales(file_path):
    """
    Reads a JSONL file, extracts sales figures, and computes the total sales.
    """
    try:
        total_sales = 0
        with open(file_path, 'r') as file:
            for line in file:
                try:
                    entry = json.loads(line.strip())  # Parse each line as JSON
                    if isinstance(entry.get("sales"), (int, float)):
                        total_sales += entry["sales"]
                except json.JSONDecodeError:
                    print("Skipping invalid JSON line")
        
        return total_sales
    except Exception as e:
        print(f"Error processing the file: {e}")
        return None

# Example usage
file_path = "q-parse-partial-json.jsonl"  # Update with the correct path
total_sales = calculate_total_sales(file_path)
print(f"Total Sales: {total_sales}")