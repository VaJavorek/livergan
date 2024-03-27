import os
import shutil

def copy_files_to_destination_folder(source_folder, destination_folder):
    # Iterate through all subfolders and their contents in the source folder
    for dirpath, _, filenames in os.walk(source_folder):
        for filename in filenames:
            # Construct the source and destination paths
            source_path = os.path.join(dirpath, filename)
            destination_path = os.path.join(destination_folder, filename)
            
            # Create the destination folder if it doesn't exist
            os.makedirs(os.path.dirname(destination_path), exist_ok=True)
            
            # Copy the file to the destination folder
            shutil.copy(source_path, destination_path)
            print(f"Copied {filename} to {destination_path}")

# Specify the source folder (current folder in this case)
source_folder = "./data/pngdata/splits_live"  # Current folder
# Specify the destination folder (change this to your desired folder)
destination_folder = "./data/custom_dataset/B"

# Call the function to copy files to the destination folder
copy_files_to_destination_folder(source_folder, destination_folder)
