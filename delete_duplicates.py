import os


# delete duplicate files in repository folder
def delete_files_with_parentheses(directory):
    for filename in os.listdir(directory):
        if "(" in filename and ")" in filename:
            file_path = os.path.join(directory, filename)
            os.remove(file_path)
            print(f"Deleted file: {file_path}")


if __name__ == "__main__":
    pass
