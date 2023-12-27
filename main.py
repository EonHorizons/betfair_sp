import wget
import os
import re
import datetime
import json
import delete_duplicates as dd
from icecream import ic
import get_bsp_files as bsp
import current_data as cd
import compare_json as cj


# Function to determine the correct folder path based on the filename
def get_folder_path(filename, base_path):
    if 'greyhound' in filename:
        # Greyhound files structure: data/greyhound/year/month
        match = re.search(r"dwbfgreyhound(win|place|placed)(\d{8}).csv", filename)
        if match:
            date = datetime.datetime.strptime(match.group(2), '%d%m%Y')
            return os.path.join(base_path, str(date.year), f"{date.month:02d}")
    else:
        # Horse racing files structure: data/horse/country/year/month
        match = re.search(r"dwbfprices(\w+)(win|place|placed)(\d{8}).csv", filename)
        if match:
            country_code = match.group(1)
            date = datetime.datetime.strptime(match.group(3), '%d%m%Y')
            return os.path.join(base_path, 'horse', country_code, str(date.year), f"{date.month:02d}")
    return None

# Function to load missing files from JSON
def load_missing_files(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Function to download files
def download_files(file_list, base_path, url):
    for sport_type, files in file_list.items():
        for file in files:
            # Correctly form the download path based on the sport type
            if sport_type == 'greyhound':
                download_path = get_folder_path(file, os.path.join(base_path, sport_type))
            else:  # For horse and other types
                download_path = get_folder_path(file, base_path)
            if download_path:
                os.makedirs(download_path, exist_ok=True)
                file_url = url + file
                try:
                    wget.download(file_url, out=os.path.join(download_path, file), bar=wget.bar_adaptive)
                except Exception as e:
                    ic(f"Failed to download {file_url}: {e}")


# Run the script
if __name__ == "__main__":

    # Website URL
    url = 'https://promo.betfair.com/betfairsp/prices/'

    # ? local pc path
    # base_path = './data'
    # ? Github Actions Path
    base_path = 'data/'

    # Get BSP website updated file list 
    bsp.create_webpage_data_json()
    # get current data folder file list
    cd.create_data_folder_json()
    # get missing files list
    cj.compare_files()

    # Load missing files list
    missing_files_path = os.path.join(base_path, 'missing_files.json')
    missing_files = load_missing_files(missing_files_path)

    # Download missing files
    download_files(missing_files, base_path, url)

    # Delete any duplicates in the GitHub repo
    dd.delete_unwanted_files()