"""
Centralized configuration for Betfair SP data management.
All paths and constants should be imported from this module.
"""

import os

# Base paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data_original')

# Data subdirectories
GREYHOUND_DIR = os.path.join(DATA_DIR, 'greyhound')
HORSE_DIR = os.path.join(DATA_DIR, 'horse')

# JSON metadata files
WEBPAGE_DATA_JSON = os.path.join(DATA_DIR, 'webpage_data.json')
DATA_FOLDER_JSON = os.path.join(DATA_DIR, 'data_folder_files.json')
MISSING_FILES_JSON = os.path.join(DATA_DIR, 'missing_files.json')
CSV_FILES_JSON = os.path.join(DATA_DIR, 'csv_files_in_data.json')

# Betfair source URL
BETFAIR_BSP_URL = 'https://promo.betfair.com/betfairsp/prices/'

# Supported countries for horse racing
HORSE_RACING_COUNTRIES = ['aus', 'uk', 'rsa', 'usa', 'ire', 'fr', 'uae']

# Request headers for web scraping
REQUEST_HEADERS = {
    'Origin': 'https://promo.betfair.com',
    'Referer': 'https://promo.betfair.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}


def ensure_data_dirs_exist():
    """Create data directories if they don't exist."""
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(GREYHOUND_DIR, exist_ok=True)
    os.makedirs(HORSE_DIR, exist_ok=True)


def get_greyhound_path(year: int, month: int) -> str:
    """Get the path for greyhound data files."""
    return os.path.join(GREYHOUND_DIR, str(year), f"{month:02d}")


def get_horse_path(country: str, year: int, month: int) -> str:
    """Get the path for horse racing data files."""
    return os.path.join(HORSE_DIR, country, str(year), f"{month:02d}")


if __name__ == "__main__":
    # Print configuration for debugging
    print(f"BASE_DIR: {BASE_DIR}")
    print(f"DATA_DIR: {DATA_DIR}")
    print(f"GREYHOUND_DIR: {GREYHOUND_DIR}")
    print(f"HORSE_DIR: {HORSE_DIR}")
    print(f"BETFAIR_BSP_URL: {BETFAIR_BSP_URL}")
