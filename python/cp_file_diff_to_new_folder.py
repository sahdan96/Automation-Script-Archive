import os
import shutil

folder_a_path = '/path/to/folder/A'
folder_b_path = '/path/to/folder/B'
output_folder = '/path/to/output_folder'

# Get the list of image files in folder A
folder_a_files = [f for f in os.listdir(folder_a_path) if os.path.isfile(os.path.join(folder_a_path, f))]

# Get the list of image files in folder B
folder_b_files = [f for f in os.listdir(folder_b_path) if os.path.isfile(os.path.join(folder_b_path, f))]

# Find the image files in folder A that are not present in folder B
missing_files = [f for f in folder_a_files if f not in folder_b_files]

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Copy the missing files to the output folder
for file_name in missing_files:
    source_file = os.path.join(folder_a_path, file_name)
    destination_file = os.path.join(output_folder, file_name)
    shutil.copy2(source_file, destination_file)

print('Comparison completed. Different files copied to', output_folder)
