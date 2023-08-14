import os
import shutil

# Set the paths for the source and destination folders
source_folder = 'data/labels'
destination_folder = 'data/train'

# Get a list of all .jpg files in the destination folder (without extensions)
destination_jpg_files = [os.path.splitext(file)[0] for file in os.listdir(destination_folder) if file.lower().endswith('.jpg')]

# Loop through the .jpg files in the destination folder
for jpg_name in destination_jpg_files:
    txt_file = jpg_name + '.txt'
    txt_source_path = os.path.join(source_folder, txt_file)
    txt_destination_path = os.path.join(destination_folder, txt_file)
    
    # Check if the corresponding .txt file exists in the source folder
    if os.path.exists(txt_source_path):
        shutil.copy(txt_source_path, txt_destination_path)
        print(f"Copying {txt_file} to the destination folder.")

print("Copying of .txt files completed.")
