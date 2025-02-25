import json

def count_key_occurrences(data, target_key):
    """Recursively count occurrences of target_key in a nested JSON object."""
    count = 0

    if isinstance(data, dict):
        for key, value in data.items():
            if key == target_key:
                count += 1
            count += count_key_occurrences(value, target_key)  # Recurse into values

    elif isinstance(data, list):
        for item in data:
            count += count_key_occurrences(item, target_key)  # Recurse into list items

    return count

# Load JSON data from file
file_path = "q-extract-nested-json-keys.json"  # Update the path if needed
with open(file_path, "r", encoding="utf-8") as file:
    try:
        json_data = json.load(file)  # Load JSON file
        result = count_key_occurrences(json_data, "DEWN")  # Count occurrences of "DEWN"
        print("Total occurrences of 'DEWN' as a key:", result)

    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)