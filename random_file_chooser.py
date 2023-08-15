# Script that randomly selects n files from a folder and moves them to another 

import os
import random
import shutil

# Source and destination folders
source_folder = 'C:\\Users\\charl\\OneDrive\\Documents\\GitHub\\vietnam_traffic_signs_dataset\\data\\test'
destination_folder = 'C:\\Users\\charl\\OneDrive\\Documents\\GitHub\\vietnam_traffic_signs_dataset\\data\\val'

# List all .jpg files in the source folder
jpg_files = [file for file in os.listdir(source_folder) if file.lower().endswith('.jpg')]

# Choose 100 random files
selected_files = random.sample(jpg_files, 1180)

# Create the destination folder if it doesn't exist
# os.makedirs(destination_folder, exist_ok=True)

# Move selected files to the destination folder
for file in selected_files:
    source_path = os.path.join(source_folder, file)
    destination_path = os.path.join(destination_folder, file)
    shutil.move(source_path, destination_path)
    print(f"Moved {file} to {destination_folder}")

print("Move operation completed.")
