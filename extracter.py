import os
import zipfile
import rarfile
import tarfile


# Specify the path to the unrar tool (if needed)
rarfile.UNRAR_TOOL = "C:\\Users\\HP\\unrarw64.exe"

def clean_filename(filename):
    """Preprocess the filename to remove extra '.zip', '.rar', or spaces."""
    # Remove leading/trailing spaces
    cleaned_name = filename.strip()
    
    # If there's an extra ".zip.zip" or ".rar.rar" at the end, clean it
    if cleaned_name.endswith('.zip.zip'):
        cleaned_name = cleaned_name[:-4]  # Remove the extra ".zip"
    elif cleaned_name.endswith('.rar.rar'):
        cleaned_name = cleaned_name[:-4]  # Remove the extra ".rar"
    
    # Remove multiple spaces
    cleaned_name = ' '.join(cleaned_name.split())
    
    return cleaned_name

def get_unique_filename(file_path):
    """Check if a file already exists and append a number to make it unique."""
    base, ext = os.path.splitext(file_path)
    counter = 1
    new_file_path = file_path
    
    while os.path.exists(new_file_path):
        new_file_path = f"{base}_{counter}{ext}"
        counter += 1
    
    return new_file_path

def unzip_file(file_name, extract_to):
    """Unzip a zip file into the specified folder."""
    with zipfile.ZipFile(file_name, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def unrar_file(file_name, extract_to):
    """Unrar a rar file into the specified folder."""
    with rarfile.RarFile(file_name, 'r') as rar_ref:
        rar_ref.extractall(extract_to)

def untar_file(file_name, extract_to):
    """Extract a tar.gz file into the specified folder."""
    with tarfile.open(file_name, 'r:gz') as tar_ref:
        tar_ref.extractall(extract_to)

# Get current working directory
cwd = os.getcwd()

# Path for the extracted files
extracted_folder = os.path.join(cwd, 'EXTRACTED')

# Create the 'EXTRACTED' folder if it doesn't already exist
if not os.path.exists(extracted_folder):
    os.makedirs(extracted_folder)

# List to keep track of files that threw errors
error_files = []

# Iterate over all files in the directory
for file in os.listdir(cwd):
    file_path = os.path.join(cwd, file)
    
    # Skip the 'EXTRACTED' folder to avoid recursion
    if file == 'EXTRACTED':
        continue
    
    # Clean up the file name (remove extra .zip/.rar and spaces)
    cleaned_file = clean_filename(file)
    
    # Handle any renaming of the file if necessary
    if cleaned_file != file:
        # Get unique file name if the cleaned name already exists
        cleaned_file_path = os.path.join(cwd, cleaned_file)
        cleaned_file_path = get_unique_filename(cleaned_file_path)
        
        # Rename the file if needed
        os.rename(file_path, cleaned_file_path)
        file_path = cleaned_file_path
        file = os.path.basename(cleaned_file_path)

    # Get the base name of the file (without extension) to create the new folder
    base_name, ext = os.path.splitext(file)
    
    # Special handling for tar.gz files
    if ext == '.gz' and file.endswith('.tar.gz'):
        base_name = file[:-7]
    
    # Strip leading/trailing spaces from base_name
    base_name = base_name.strip()

    # Create a new folder inside 'EXTRACTED' with the name of the archive (without extension)
    extract_to = os.path.join(extracted_folder, base_name)
    
    # Create the folder if it doesn't already exist
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)
    
    try:
        # Check file type and extract accordingly
        if file.endswith('.zip'):
            print(f"Extracting {file} to {extract_to}...")
            unzip_file(file_path, extract_to)
        elif file.endswith('.rar'):
            print(f"Extracting {file} to {extract_to}...")
            unrar_file(file_path, extract_to)
        elif file.endswith('.tar.gz'):
            print(f"Extracting {file} to {extract_to}...")
            untar_file(file_path, extract_to)
        else:
            print(f"Skipping {file}, not a supported archive format.")
    
    except Exception as e:
        print(f"Error extracting {file}: {e}")
        error_files.append(file)

# Print the list of files that caused errors
if error_files:
    print("\nThe following files threw errors during extraction:")
    for error_file in error_files:
        print(error_file)
else:
    print("\nAll files were extracted successfully.")
