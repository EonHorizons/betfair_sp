import requests
from lxml import html
import wget
import os
import delete_duplicates as dd
import re
import datetime


# Website URL
url = 'promo.betfair.com/betfairsp/prices/'

# Github actions workflow folder destination
# download_folder = 'data/'

# local pc  path
download_folder = './data/test'  # Adjust the path as necessary
base_path = './data/test'  # Adjust the path as necessary

# Codespace folder destination
# download_folder = '/workspaces/betfair_sp/data'

# GET request to webpage to retrieve  HTML content
response = requests.get(url)

# Parse HTML with  lxml library's html module
doc = html.fromstring(response.text)

# Step: Extract  text from HTML
text = doc.text_content()

# Create list of csv files
csv_links = [word for word in text.split() if word.endswith('.csv')]


# Download files not yet downloaded. BSP webpage has more than 50k files.
# todo update code to check for latest file names and not all csv files listed on BSP page
def download_new():
    # Get list of all CSV files already downloaded
    downloaded_files = [f for f in os.listdir(
        download_folder) if f.endswith('.csv')]

    # loop csv links and download files not yet downloaded
    for link in csv_links:
        if link not in downloaded_files:

            wget.download(url+link, out=download_folder, bar=None)


def get_folder_path(filename, base_path):
    match = re.search(r"dwbf(\w+)(\d{8}).csv", filename)
    if match:
        country_code = match.group(1)[:3]  # Extract the first three letters for country code
        date = datetime.datetime.strptime(match.group(2), '%d%m%Y')
        return os.path.join(base_path, country_code, str(date.year), f"{date.month:02d}")
    return None



# Run the script
if __name__ == "__main__":

    # Download files not yet downloaded - Github actions workflow option only.
    download_new()

    # delete any duplicates in github repo
    dd.delete_files_not_ending_with_csv(download_folder)
    dd.delete_files_with_parentheses(download_folder)

