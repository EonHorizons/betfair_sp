import os


# Github repo folder destination
# download_folder = 'data/'
download_folder = '/workspaces/betfair_sp/data'

# delete duplicate files in repository folder
def delete_files_with_parentheses(directory):
    """ Deletes all files in the given directory whose name contains parentheses. """
    for filename in os.listdir(directory):
        if "(" in filename and ")" in filename:
            file_path = os.path.join(directory, filename)
            os.remove(file_path)
            print(f"Deleted file: {file_path}")

 
def delete_files_not_ending_with_csv(directory):
    """ Deletes all files in the given directory whose name does not end with ".csv". """
    for filename in os.listdir(directory):
        if not filename.endswith(".csv"):
            file_path = os.path.join(directory, filename)
            os.remove(file_path)
            print(f"Deleted file: {file_path}")


if __name__ == "__main__":
    delete_files_with_parentheses(download_folder)
    delete_files_not_ending_with_csv(download_folder)
