import os
import zipfile
import tarfile
import rarfile
import py7zr



# Define the list of file extensions to search for
file_extensions = ['.zip', '.rar', '.7z', '.tar.gz']

# Function to unzip/extract files
def unzip_file(file_path):
    try:
        # Handle .zip files
        if file_path.endswith('.zip'):
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                extract_to = os.path.splitext(file_path)[0]
                zip_ref.extractall(extract_to)
                print(f"Extracted {file_path} to {extract_to}")
        
        # Handle .tar.gz files
        elif file_path.endswith('.tar.gz'):
            with tarfile.open(file_path, 'r:gz') as tar_ref:
                extract_to = os.path.splitext(file_path)[0]
                tar_ref.extractall(extract_to)
                print(f"Extracted {file_path} to {extract_to}")
        
        # Handle .rar files
        elif file_path.endswith('.rar'):
            with rarfile.RarFile(file_path, 'r') as rar_ref:
                extract_to = os.path.splitext(file_path)[0]
                rar_ref.extractall(extract_to)
                print(f"Extracted {file_path} to {extract_to}")
        
        # Handle .7z files
        elif file_path.endswith('.7z'):
            with py7zr.SevenZipFile(file_path, mode='r') as z_ref:
                extract_to = os.path.splitext(file_path)[0]
                z_ref.extractall(extract_to)
                print(f"Extracted {file_path} to {extract_to}")

    except Exception as e:
        print(f"Error extracting {file_path}: {e}")

# Function to recursively check for archive files
def find_and_unzip_files(start_dir):
    for root, dirs, files in os.walk(start_dir):
        for file in files:
            if any(file.endswith(ext) for ext in file_extensions):
                file_path = os.path.join(root, file)
                unzip_file(file_path)

# Get the current working directory
cwd = os.getcwd()

# Call the function to search and unzip in the cwd
find_and_unzip_files(cwd)
