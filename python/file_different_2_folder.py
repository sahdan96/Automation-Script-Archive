import os

folder_a_path = '/path/to/folder/A'
folder_b_path = '/path/to/folder/B'
output_file = '/path/to/output.txt'

# Get the list of image files in folder A
folder_a_files = [f for f in os.listdir(folder_a_path) if os.path.isfile(os.path.join(folder_a_path, f))]

# Get the list of image files in folder B
folder_b_files = [f for f in os.listdir(folder_b_path) if os.path.isfile(os.path.join(folder_b_path, f))]

# Find the image files in folder A that are not present in folder B
missing_files = [f for f in folder_a_files if f not in folder_b_files]

# Write the missing file names to the output file
with open(output_file, 'w') as file:
    file.write('\n'.join(missing_files))

print('Comparison completed. Missing files listed in', output_file)
