import re
import gzip
from datetime import datetime

# Define the log file
log_file = "s-anand.net-May-2024.gz"

# Regex pattern to extract relevant fields
log_pattern = re.compile(
    r'\[(\d{2})/May/2024:(\d{2}):\d{2}:\d{2} .*?\] "GET (/telugu/[^"]*) HTTP/1.\d" (\d{3})'
)

# Counter for successful GET requests
count = 0

# Open and process the log file
with gzip.open(log_file, 'rt', encoding='utf-8', errors='ignore') as f:
    for line in f:
        match = log_pattern.search(line)
        if match:
            day, hour, url, status = match.groups()
            day, hour, status = int(day), int(hour), int(status)

            # Convert day number to the day of the week
            date_obj = datetime(2024, 5, day)
            if date_obj.strftime("%A") == "Saturday" and 11 <= hour < 15 and 200 <= status < 300:
                count += 1

# Print result
print(f"Successful GET requests for /telugu/ on Saturdays between 11:00-14:59: {count}")
