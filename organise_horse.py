import os
import shutil
import re
import datetime




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


def reorganize_horse_racing_files(base_path):
    horse_base_path = os.path.join(base_path, 'horse')
    for year_folder in os.listdir(horse_base_path):
        year_path = os.path.join(horse_base_path, year_folder)
        if os.path.isdir(year_path):
            for month_folder in os.listdir(year_path):
                month_path = os.path.join(year_path, month_folder)
                if os.path.isdir(month_path):
                    for file in os.listdir(month_path):
                        if file.endswith('.csv') and not 'greyhound' in file:
                            try:
                                new_path = get_folder_path(file, base_path)
                                if new_path:
                                    os.makedirs(new_path, exist_ok=True)
                                    src = os.path.join(month_path, file)
                                    dest = os.path.join(new_path, file)
                                    # print(f"Moving {src} to {dest}")
                                    shutil.move(src, dest)
                            except Exception as e:
                                print(f"Error moving file {file}: {e}")



base_path = './data'  # Base path for your data

# Run the script
reorganize_horse_racing_files(base_path)

