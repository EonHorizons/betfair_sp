import requests
from lxml import html
import json

def create_webpage_data_json(url, output_json_path):
    # GET request to webpage to retrieve HTML content
    response = requests.get(url)

    # if response.status_code != 200:
    #     raise Exception(f"Failed to fetch webpage: Status code {response.status_code}")

    # Parse HTML with lxml library's html module
    doc = html.fromstring(response.text)

    # Extract CSV file links from HTML
    csv_links = [word for word in doc.text_content().split() if word.endswith('.csv')]

    # Save the list to a JSON file
    with open(output_json_path, 'w') as file:
        json.dump(csv_links, file)

    print(f"Saved webpage data to {output_json_path}")

# URL of the Betfair Starting Price (BSP) webpage
url = 'https://promo.betfair.com/betfairsp/prices'
# https://promo.betfair.com/betfairsp/prices

# JSON file path to store the list of files from the webpage inside the data folder
output_json_path = './data/webpage_data.json'

# Run the script
create_webpage_data_json(url, output_json_path)
