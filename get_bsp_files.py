import requests
from lxml import html
import json
import urllib.request

def check_access():
    # URL to be accessed
    url = 'https://promo.betfair.com/betfairsp/prices'

    # Creating a Request object with the specified URL
    req = urllib.request.Request(url)

    # Adding necessary headers to the Request object
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36')
    req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9')
    req.add_header('Accept-Language', 'en-US,en;q=0.9')
    req.add_header('Cache-Control', 'max-age=0')
    # Add other headers as needed

    # Sending the request and reading the response
    response = urllib.request.urlopen(req).read().decode('utf-8')

    # Writing the response to an HTML file
    with open("test.html", 'w', encoding="utf-8") as f:
        f.write(response)




def create_webpage_data_json():

    # ? JSON file path for Betfair Starting Price file list

    # ? Local Path
    # output_json_path = './data/webpage_data.json'

    # ? Github Path
    output_json_path = 'data/webpage_data.json'

    # URL of the Betfair Starting Price (BSP) webpage
    url = 'https://promo.betfair.com/betfairsp/prices'

        # Headers with User-Agent
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'dnt': '1',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',    
    'Origin' : 'https://promo.betfair.com',
    'Referer' : 'https://promo.betfair.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}
    # headers = {
    #     'Origin' : 'https://promo.betfair.com',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    #     'Referer' : 'https://promo.betfair.com/'
    #     }

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
