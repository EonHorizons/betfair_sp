import os
import datetime

def create_folder_structure(base_path, countries, start_year, end_year):
    for country in countries:
        for year in range(start_year, end_year + 1):
            for month in range(1, 13):
                folder_path = os.path.join(base_path, country, str(year), f"{month:02d}")
                os.makedirs(folder_path, exist_ok=True)

# Usage
base_path = './data'
countries = ['aus', 'uk', 'rsa', 'usa', 'ire', 'fr', 'uae']
start_year = 2008
end_year = datetime.datetime.now().year
create_folder_structure(base_path, countries, start_year, end_year)
