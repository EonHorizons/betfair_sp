import requests
from lxml import html
import json
import config


def create_webpage_data_json():
    """Fetch the list of available BSP files from Betfair website and save to JSON."""

    # URL of the Betfair Starting Price (BSP) webpage (without trailing slash for page)
    url = config.BETFAIR_BSP_URL.rstrip('/')

    # GET request to webpage to retrieve HTML content
    response = requests.get(url, headers=config.REQUEST_HEADERS)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch webpage: Status code {response.status_code}")

    # Parse HTML with lxml library's html module
    doc = html.fromstring(response.text)

    # Extract CSV file links from HTML
    csv_links = [word for word in doc.text_content().split() if word.endswith('.csv')]

    # Save the list to a JSON file
    with open(config.WEBPAGE_DATA_JSON, 'w') as file:
        json.dump(csv_links, file)

    print(f"Saved webpage data to {config.WEBPAGE_DATA_JSON}")


if __name__ == "__main__":
    # Run the script
    create_webpage_data_json()
    # check_access()
