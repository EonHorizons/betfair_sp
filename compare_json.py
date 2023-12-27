import json

def load_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def find_missing_files():


    # ? Load JSON files
    # ? Local Path
    webpage_json = load_json_file('./data/webpage_data.json')
    local_data_json = load_json_file('./data/data_folder_files.json')

    # ? Github Path
    # webpage_json = load_json_file('data/webpage_data.json')
    # local_data_json = load_json_file('data/data_folder_files.json')


    missing_files = {"greyhound": [], "horse": []}

    # Extract all local file paths for greyhound and horse
    local_greyhound_files = sum([month_files for year in local_data_json["greyhound"].values() 
                                 for month_files in year.values()], [])
    local_horse_files = sum([month_files for country in local_data_json["horse"].values() 
                             for year in country.values() 
                             for month_files in year.values()], [])

    # Compare with webpage files
    for file in webpage_json:
        if 'greyhound' in file and file not in local_greyhound_files:
            missing_files["greyhound"].append(file)
        elif 'prices' in file and file not in local_horse_files:
            missing_files["horse"].append(file)

    return missing_files


def save_json_file(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file)


def compare_files():
    # Find missing files
    missing_files = find_missing_files()

    # ? Save the missing files as JSON
    # ?Local Path
    missing_files_json_path = './data/missing_files.json'

    # ?Github Actions Path
    # missing_files_json_path = 'data/missing_files.json'
    
    save_json_file(missing_files, missing_files_json_path)

    print(f"Missing files saved to {missing_files_json_path}")

    # Output the missing files
    print("Missing Greyhound Files:", missing_files["greyhound"])
    print("Missing Horse Files:", missing_files["horse"])


if __name__ == "__main__":
    compare_files()
