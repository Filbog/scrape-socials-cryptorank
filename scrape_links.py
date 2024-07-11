import requests
from bs4 import BeautifulSoup
import json

# URL of the webpage
url = "https://cryptorank.io/funds/vitalik-buterin"  # Replace with the actual URL

# Send a GET request to the webpage
response = requests.get(url)
response.raise_for_status()  # Check for HTTP errors

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Find the <script> tag with id='__NEXT_DATA__'
script_tag = soup.find("script", id="__NEXT_DATA__")

# Extract the JSON content from the <script> tag
json_content = script_tag.string

# Parse the JSON content
data = json.loads(json_content)

# Extract the "links" values
links = data["props"]["pageProps"]["fund"]["links"]

# Save the extracted links to a JSON file
with open("links.json", "w") as file:
    json.dump(links, file, indent=4)

# Print the extracted links
for link in links:
    print(f"Type: {link['type']}, Value: {link['value']}")
