import os
import json


def create_nested_structure_for_greyhound_files(root_path):
    nested_structure = {}
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

def create_data_folder_json(data_folder_path, output_json_path):
    structured_files = {"greyhound": {}, "horse": {}}

    # Greyhound files with simplified structure
    greyhound_path = os.path.join(data_folder_path, "greyhound")
    structured_files["greyhound"] = create_nested_structure_for_greyhound_files(greyhound_path)

    # Horse files with nested structure (not changed)
    horse_path = os.path.join(data_folder_path, "horse")
    structured_files["horse"] = create_nested_structure_for_horse_files(horse_path)

    with open(output_json_path, 'w') as file:
        json.dump(structured_files, file)

    print(f"Saved data folder content to {output_json_path}")




# Path to the data folder
data_folder_path = './data'

# JSON file path to store the structured list of files from the data folder
output_json_path = './data/data_folder_files.json'

# Run the script
create_data_folder_json(data_folder_path, output_json_path)
