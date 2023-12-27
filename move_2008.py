import os
import shutil
import re
import datetime


def move_2008_files(base_path, year):
    source_folder = os.path.join(base_path, year)
    horse_folder = os.path.join(base_path, 'horse')

    for file in os.listdir(source_folder):
        # Identify country based on filename
        country_code = 'uk'  # Default to UK
        if 'ire' in file:
            country_code = 'ire'

        # Extract date and construct new path
        match = re.search(r"(\d{8}).csv", file)
        if match:
            date = datetime.datetime.strptime(match.group(1), '%d%m%Y')
            new_path = os.path.join(horse_folder, country_code, str(date.year), f"{date.month:02d}")

            # Move file
            if not os.path.exists(new_path):
                os.makedirs(new_path, exist_ok=True)
            shutil.move(os.path.join(source_folder, file), os.path.join(new_path, file))

# Paths
base_path = './data'
year = '2008'

# Move the 2008 files
move_2008_files(base_path, year)
