import json
import os

def generate_initial_downloaded_files_json(base_path, json_file_path):
    downloaded_files = get_all_csv_files(base_path)
    save_downloaded_files(json_file_path, downloaded_files)

def get_all_csv_files(directory):
    csv_files = set()
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.csv'):
                csv_files.add(file)
    return csv_files

def save_downloaded_files(file_path, downloaded_files):
    with open(file_path, 'w') as file:
        json.dump(list(downloaded_files), file)

# Run the script to generate initial JSON
if __name__ == "__main__":
    base_path = './data_original'  # Adjust this to your data directory path
    json_file_path = os.path.join(base_path, 'downloaded_files.json')
    generate_initial_downloaded_files_json(base_path, json_file_path)
