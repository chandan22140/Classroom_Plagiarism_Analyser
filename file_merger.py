import os

# Define the PROCESSED directory path
cwd = os.getcwd()
processed_dir = os.path.join(cwd, 'PROCESSED')

def merge_java_files():
    # Iterate through each subfolder in the PROCESSED directory
    for folder in os.listdir(processed_dir):
        folder_path = os.path.join(processed_dir, folder)
        
        # Skip if it's not a folder
        if not os.path.isdir(folder_path):
            continue

        # Initialize an empty string to collect file contents
        merged_content = ""
        
        # Iterate through all files in the subfolder
        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".java"):
                    file_path = os.path.join(root, file)
                    
                    # Attempt to read the file content with UTF-8, fallback if it fails
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            merged_content += f.read() + f"\n // {file} ended \n"
                    except UnicodeDecodeError:
                        with open(file_path, 'r', encoding='ISO-8859-1', errors='ignore') as f:
                            merged_content += f.read() + f"\n // {file} ended \n"

        # Define the merged file path using the folder name
        merged_file_path = os.path.join(processed_dir, f"{folder}_merged.java")
        
        # Write the merged content to a new .java file
        with open(merged_file_path, 'w', encoding='utf-8') as merged_file:
            merged_file.write(merged_content)
        
        print(f"Merged files in '{folder}' into '{merged_file_path}'")

# Run the merging function
merge_java_files()
