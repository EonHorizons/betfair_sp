import json
import config


def load_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def find_missing_files():
    """Compare webpage files with local files and return missing files."""

    # Load JSON files using config paths
    webpage_json = load_json_file(config.WEBPAGE_DATA_JSON)
    local_data_json = load_json_file(config.DATA_FOLDER_JSON)


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
    """Find missing files and save to JSON."""
    # Find missing files
    missing_files = find_missing_files()

    # Save the missing files as JSON
    save_json_file(missing_files, config.MISSING_FILES_JSON)

    print(f"Missing files saved to {config.MISSING_FILES_JSON}")

    # Output the missing files
    print("Missing Greyhound Files:", missing_files["greyhound"])
    print("Missing Horse Files:", missing_files["horse"])


if __name__ == "__main__":
    compare_files()
