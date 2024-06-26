import requests
from lxml import html
import json


def create_webpage_data_json():

    # ? JSON file path for Betfair Starting Price file list

    # ? Local Path
    # output_json_path = './data/webpage_data.json'

    # ? Github Path
    output_json_path = 'data_original/webpage_data.json'

    # URL of the Betfair Starting Price (BSP) webpage
    url = 'https://promo.betfair.com/betfairsp/prices'

        # Headers with User-Agent
    headers = {
    'Origin' : 'https://promo.betfair.com',
    'Referer' : 'https://promo.betfair.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}


    # GET request to webpage to retrieve HTML content
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch webpage: Status code {response.status_code}")

    # Parse HTML with lxml library's html module
    doc = html.fromstring(response.text)

    # Extract CSV file links from HTML
    csv_links = [word for word in doc.text_content().split() if word.endswith('.csv')]

    # Save the list to a JSON file
    with open(output_json_path, 'w') as file:
        json.dump(csv_links, file)

    print(f"Saved webpage data to {output_json_path}")


if __name__ == "__main__":
    # Run the script
    create_webpage_data_json()
    # check_access()
