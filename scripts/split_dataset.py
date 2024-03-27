import os
import shutil
import random
import math

def split_dataset(input_folder, train_folder, test_folder, split_ratio=0.8):
    # Create destination folders if they don't exist
    os.makedirs(train_folder, exist_ok=True)
    os.makedirs(test_folder, exist_ok=True)

    # Get the list of files in the input folder
    files = os.listdir(input_folder)
    num_files = len(files)
    num_train_files = math.ceil(num_files * split_ratio)
    num_test_files = num_files - num_train_files

    # Shuffle the files randomly
    random.shuffle(files)

    # Split the files into training and testing sets
    train_files = files[:num_train_files]
    test_files = files[num_train_files:]

    # Copy training files to the training folder
    for file in train_files:
        source_path = os.path.join(input_folder, file)
        destination_path = os.path.join(train_folder, file)
        shutil.copy(source_path, destination_path)
        print(f'File {file} copied for training.')

    # Copy testing files to the testing folder
    for file in test_files:
        source_path = os.path.join(input_folder, file)
        destination_path = os.path.join(test_folder, file)
        shutil.copy(source_path, destination_path)
        print(f'File {file} copied for testing.')

    print(f"Dataset split completed: {num_train_files} files for training, {num_test_files} files for testing.")

# Specify the input folder containing the dataset (change this to your dataset folder)
# input_folder = "./data/custom_dataset/A"
input_folder = "./data/custom_dataset/B"
# Specify the folders for training and testing datasets
# train_folder = "./data/custom_dataset/trainA"
# test_folder = "./data/custom_dataset/testA"
train_folder = "./data/custom_dataset/trainB"
test_folder = "./data/custom_dataset/testB"

# Split the dataset and copy files to the respective folders
split_dataset(input_folder, train_folder, test_folder, split_ratio=0.8)