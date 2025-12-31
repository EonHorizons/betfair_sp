import os
import config


def delete_files_with_parentheses(directory):
    """Deletes all files in the given directory and subdirectories whose name contains parentheses."""
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if "(" in filename and ")" in filename:
                file_path = os.path.join(root, filename)
                os.remove(file_path)
                print(f"Deleted file: {file_path}")


def delete_files_not_ending_with_csv(directory):
    """Deletes all files in the given directory and subdirectories whose name does not end with .csv or .json."""
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if not filename.endswith(".csv") and not filename.endswith(".json"):
                file_path = os.path.join(root, filename)
                os.remove(file_path)
                print(f"Deleted file: {file_path}")


def delete_unwanted_files():
    """Delete duplicate files and non-CSV/JSON files from the data directory."""
    delete_files_with_parentheses(config.DATA_DIR)
    delete_files_not_ending_with_csv(config.DATA_DIR)



if __name__ == "__main__":
    delete_unwanted_files()

