import requests
from lxml import html
import wget
import datetime
import os
import delete_duplicates as dd

# todo check os required in requirements.txt

# Website URL
url = 'https://promo.betfair.com/betfairsp/prices/'

# Github repo folder destination
download_folder = '/workspaces/betfair_sp/data'

# GET request to webpage to retrieve  HTML content
response = requests.get(url)

# Parse HTML with  lxml library's html module
doc = html.fromstring(response.text)

# Step: Extract  text from HTML
text = doc.text_content()

# Create list of csv files
csv_links = [word for word in text.split() if word.endswith('.csv')]


# 1st download option - Download all files to destination folder
# ! Beware more than 50,000 files in this option
def download_all():
    for link in csv_links:
        wget.download(url+link, download_folder, bar=None)


# 2nd download option: Download files between a date range
def download_range(start_date=None, end_date=None):
    for link in csv_links:
        # Extract date from filename
        file_date = datetime.datetime.strptime(
            link[-12:-4], '%d%m%Y')
        # Download the file if it falls within the date range
        if start_date <= file_date <= end_date:
            wget.download(url+link, out=download_folder, bar=None)
        elif file_date < start_date:
            break


# 3rd download option: Download files not yet downloaded
# ! Beware - total file count is > 50,000
def download_new():
    # Get list of all CSV files already downloaded
    downloaded_files = [f for f in os.listdir(
        download_folder) if f.endswith('.csv')]

    # loop csv links and download files not yet downloaded
    for link in csv_links:
        if link not in downloaded_files:
            # Download the file
            wget.download(url+link, out=download_folder, bar=None)


# 4th download option:
# Download files most recent files not yet downloaded from oldest file in download folder
def download_newest():
    # Get list of all CSV files already downloaded
    downloaded_files = [f for f in os.listdir(
        download_folder) if f.endswith('.csv')]

    # Get most recent file already downloaded based on DDMMYYYY date format in filename
    most_recent_file = max(
        downloaded_files, key=lambda x: datetime.datetime.strptime(x[-12:-4], '%d%m%Y'))

    # Loop csv links on the website and download files not yet downloaded and more recent than the most recent file already downloaded. Break loop if file is older than most recent file already downloaded.
    for link in csv_links:
        # Extract date from filename
        file_date = datetime.datetime.strptime(
            link[-12:-4], '%d%m%Y')
        # Download the file if it falls within the date range
        if file_date > datetime.datetime.strptime(most_recent_file[-12:-4], '%d%m%Y') and link not in downloaded_files:
            # Download the file
            wget.download(url+link, download_folder, bar=None)
        else:
            break


# Wrap all options into a function
def download_files():
    print('1. Download all files')
    print('2. Download files between a date range')
    print('3. Download all files not yet downloaded')
    print('4. Download newer files not yet downloaded from most recent file in download folder')
    # option = int(input('Enter option: '))         # Uncomment this line to have user select file download method

    # Delete below code line and uncomment line above to use code interactively
    option = 4
    if option == 1:
        download_all()
    elif option == 2:
        start_date = datetime.datetime.strptime(
            input('Enter start date (DDMMYYYY): '), '%d%m%Y')
        end_date = datetime.datetime.strptime(
            input('Enter end date (DDMMYYYY): '), '%d%m%Y')
        download_range(start_date, end_date)
    elif option == 3:
        download_new()
    elif option == 4:
        download_newest()
    else:
        print('Invalid option')


# delete any duplicates
dd.delete_files_with_parentheses(download_folder)

# Run the function
if __name__ == "__main__":
    download_files()
