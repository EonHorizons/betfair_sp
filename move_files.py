import os
import shutil
import re
import datetime

def move_files_to_structure(base_path):
    for file in os.listdir(base_path):
        if file.endswith('.csv'):
            folder_path = get_folder_path(file, base_path)
            if folder_path:
                os.makedirs(folder_path, exist_ok=True)
                shutil.move(os.path.join(base_path, file), os.path.join(folder_path, file))

def get_folder_path(filename, base_path):
    match = re.search(r"dwbf(\w+)(\d{8}).csv", filename)
    if match:
        country_code = match.group(1)[:3]  # Extract the first three letters for country code
        date = datetime.datetime.strptime(match.group(2), '%d%m%Y')
        return os.path.join(base_path, country_code, str(date.year), f"{date.month:02d}")
    return None

# Run the script to move files
if __name__ == "__main__":
    base_path = './data'  # Adjust this to your data directory path
    move_files_to_structure(base_path)
