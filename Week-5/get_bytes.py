import re
import gzip
from collections import defaultdict

# Define the log file
log_file = "s-anand.net-May-2024.gz"

# Regex pattern to extract relevant fields
log_pattern = re.compile(
    r'(\d+\.\d+\.\d+\.\d+) .*? \[09/May/2024:.*?\] "GET (/carnatic/[^"]*) HTTP/1.\d" \d{3} (\d+)'
)

# Dictionary to store total bytes downloaded per IP
ip_bytes = defaultdict(int)

# Open and process the log file
with gzip.open(log_file, 'rt', encoding='utf-8', errors='ignore') as f:
    for line in f:
        match = log_pattern.search(line)
        if match:
            ip, url, size = match.groups()
            ip_bytes[ip] += int(size)

# Find the IP with the highest total bytes downloaded
top_ip, max_bytes = max(ip_bytes.items(), key=lambda x: x[1])

# Print result
print(f"Top IP address: {top_ip}")
print(f"Bytes downloaded by top IP: {max_bytes}")
