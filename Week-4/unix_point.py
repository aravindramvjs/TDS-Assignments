import requests
import xml.etree.ElementTree as ET

# Step 1: Fetch data from the HNRSS API
url = 'https://hnrss.org/newest?q=Unix&points=66'
response = requests.get(url)

# Step 2: Parse the XML response
root = ET.fromstring(response.content)

# Step 3: Extract the link from the most recent <item>
namespace = {'default': 'http://www.w3.org/2005/Atom'}
item = root.find('channel/item/link').text

print(item)
