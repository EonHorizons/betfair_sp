import requests
from lxml import html
import wget
import os
import delete_duplicates as dd
import re
import datetime
import json

# Website URL
url = 'https://promo.betfair.com/betfairsp/prices/'

# local pc path
base_path = './data'  # Adjust the path as necessary

# Function to determine the correct folder path based on the filename
def get_folder_path(filename, base_path):
    if 'greyhound' in filename:
        # Greyhound files structure: data/greyhound/year/month
        match = re.search(r"dwbfgreyhound(win|place|placed)(\d{8}).csv", filename)
        if match:
            date = datetime.datetime.strptime(match.group(2), '%d%m%Y')
            return os.path.join(base_path, 'greyhound', str(date.year), f"{date.month:02d}")
    else:
        # Horse racing files structure: data/horse/country/year/month
        match = re.search(r"dwbfprices(\w+)(win|place|placed)(\d{8}).csv", filename)
        if match:
            country_code = match.group(1)
            date = datetime.datetime.strptime(match.group(3), '%d%m%Y')
            return os.path.join(base_path, 'horse', country_code, str(date.year), f"{date.month:02d}")
    return None


# Function to read downloaded files from JSON
def read_downloaded_files(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return set(json.load(file))
    return set()

# Function to save downloaded files to JSON
def save_downloaded_files(file_path, downloaded_files):
    with open(file_path, 'w') as file:
        json.dump(list(downloaded_files), file)

# Download new files function
def download_new():
    downloaded_files_file = os.path.join(base_path, 'downloaded_files.json')
    downloaded_files = read_downloaded_files(downloaded_files_file)

    # GET request to webpage to retrieve HTML content
    response = requests.get(url)
    # Parse HTML with lxml library's html module
    doc = html.fromstring(response.text)
    # Extract text from HTML
    csv_links = [word for word in doc.text_content().split() if word.endswith('.csv')]

    # Loop csv links and download files not yet downloaded
    for link in csv_links:
        if link not in downloaded_files:
            folder_path = get_folder_path(link, base_path)
            if folder_path:
                os.makedirs(folder_path, exist_ok=True)
                wget.download(url + link, out=os.path.join(folder_path, link), bar=None)
                downloaded_files.add(link)
    
    save_downloaded_files(downloaded_files_file, downloaded_files)

# Run the script
if __name__ == "__main__":

    # Download files not yet downloaded - Github actions workflow option only.
    download_new()

    # delete any duplicates in github repo
    dd.delete_files_not_ending_with_csv(base_path)
    dd.delete_files_with_parentheses(base_path)
