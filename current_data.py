import os
import json
import config


def create_nested_structure_for_greyhound_files(root_path):
    nested_structure = {}
    print(f"Scanning directory: {root_path}")  # Debugging print
    for year in os.listdir(root_path):
        year_path = os.path.join(root_path, year)
        if os.path.isdir(year_path):
            nested_structure[year] = {}
            for month in os.listdir(year_path):
                month_path = os.path.join(year_path, month)
                if os.path.isdir(month_path):
                    files = [f for f in os.listdir(month_path) if f.endswith('.csv')]
                    nested_structure[year][month] = files
    return nested_structure


def create_nested_structure_for_horse_files(root_path):
    nested_structure = {}
    print(f"Scanning directory: {root_path}")  # Debugging print
    for first_level in os.listdir(root_path):
        first_level_path = os.path.join(root_path, first_level)
        if os.path.isdir(first_level_path):
            nested_structure[first_level] = {}
            for second_level in os.listdir(first_level_path):
                second_level_path = os.path.join(first_level_path, second_level)
                if os.path.isdir(second_level_path):
                    nested_structure[first_level][second_level] = {}
                    for third_level in os.listdir(second_level_path):
                        third_level_path = os.path.join(second_level_path, third_level)
                        if os.path.isdir(third_level_path):
                            files = [f for f in os.listdir(third_level_path) if f.endswith('.csv')]
                            nested_structure[first_level][second_level][third_level] = files
                            if not files:  # Debugging print
                                print(f"No CSV files found in {third_level_path}")
    return nested_structure

def create_data_folder_json():
    """Scan the data directory and create a JSON file with the folder structure."""

    structured_files = {"greyhound": {}, "horse": {}}

    # Greyhound files with simplified structure
    if os.path.exists(config.GREYHOUND_DIR):
        structured_files["greyhound"] = create_nested_structure_for_greyhound_files(config.GREYHOUND_DIR)

    # Horse files with nested structure
    if os.path.exists(config.HORSE_DIR):
        structured_files["horse"] = create_nested_structure_for_horse_files(config.HORSE_DIR)

    with open(config.DATA_FOLDER_JSON, 'w') as file:
        json.dump(structured_files, file)

    print(f"Saved data folder content to {config.DATA_FOLDER_JSON}")


if __name__ == "__main__":

    # Run the script
    create_data_folder_json()
