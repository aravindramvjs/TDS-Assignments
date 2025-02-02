# import chardet

# with open('data3.txt', 'rb') as f:
#     result = chardet.detect(f.read())
# print(result['encoding'])

# Windows-1252
# utf-8
# UTF-16


import os
import chardet

def detect_encoding(file_path):
    """Detect the encoding of a file using chardet."""
    with open(file_path, 'rb') as f:
        raw_data = f.read()
        result = chardet.detect(raw_data)
        return result['encoding']

def find_special_chars_and_sum(file_path, encodings=['utf-8', 'utf-16', 'windows-1252']):
    """Search for ‡ or Š in a file and calculate the sum of values associated with them."""
    special_chars = ['‡', 'Š']
    char_sums = {char: 0 for char in special_chars}
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                content = f.read()
                for char in special_chars:
                    if char in content:
                        print(f"Character '{char}' found in {file_path} using {encoding}.")
                        # Extract numerical values associated with the character
                        lines = content.splitlines()
                        for line in lines:
                            if char in line:
                                try:
                                    value = float(line.split(char)[-1].strip())
                                    char_sums[char] += value
                                except ValueError:
                                    pass
        except Exception as e:
            print(f"Error reading {file_path} with {encoding}: {e}")
    return char_sums

def main():
    """Search all files in the current directory for ‡ or Š and calculate their sums."""
    current_directory = os.getcwd()
    total_sums = {'‡': 0, 'Š': 0}
    for file_name in os.listdir(current_directory):
        file_path = os.path.join(current_directory, file_name)
        if os.path.isfile(file_path):
            print(f"Checking {file_path}...")
            encoding = detect_encoding(file_path)
            if encoding:
                print(f"Detected encoding: {encoding}")
            char_sums = find_special_chars_and_sum(file_path)
            for char in total_sums:
                total_sums[char] += char_sums[char]
    for char, total in total_sums.items():
        print(f"Total sum of values associated with '{char}': {total}")

if __name__ == "__main__":
    main()
