import os
import re

def check_files(folder_path):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)
    # Create an empty list to store the duplicate files
    duplicate_files = []
    # Iterate through each file in the folder
    for file in files:
        keyword = re.findall(r"[\w']+", file)
        keyword = [x for x in keyword if x.isalpha()] # only keep the string keyword
        # Iterate through the remaining files
        for other_file in files:
            # Skip the current file
            if file == other_file:
                continue
            # Check if the keyword is present in the other file's name
            if any(word in other_file for word in keyword):
                # If so, add the file to the list of duplicate files
                duplicate_files.append(file)
                break
    # Write the list of duplicate files to a file
    with open("duplicate_files.txt", "w") as f:
        for file in duplicate_files:
            f.write(file + "\n")



check_files("path/to/folder")
