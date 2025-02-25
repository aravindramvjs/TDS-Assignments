import re

# Get the uploaded file name
file_name = "./q-clean-up-student-marks.txt"

# Data Extraction: Read file line by line and extract student IDs
student_ids = set()
with open(file_name, 'r', encoding='utf-8') as file:
    for line in file:
        matches = re.findall(r'\b[A-Z0-9]{10}\b', line)  # Match exact 10-character alphanumeric IDs
        student_ids.update(matches)

# Reporting: Count the number of unique student IDs
print(f"Number of unique students: {len(student_ids)}")