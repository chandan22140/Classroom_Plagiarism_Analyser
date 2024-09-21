import os
import shutil

def process_folders():
    try:
        # Define the directories
        cwd = os.getcwd()
        extracted_dir = os.path.join(cwd, 'EXTRACTED')
        processed_dir = os.path.join(cwd, 'PROCESSED')

        # Create PROCESSED directory if it doesn't exist
        os.makedirs(processed_dir, exist_ok=True)

        # Iterate through the folders in the EXTRACTED directory
        for folder in os.listdir(extracted_dir):
            folder_path = os.path.join(extracted_dir, folder)

            # Skip if it's not a folder
            if not os.path.isdir(folder_path):
                continue

            try:
                # Extract the base name without variations (x)
                base_name = folder.split('(')[0]

                # Create corresponding folder in PROCESSED directory
                processed_folder_path = os.path.join(processed_dir, base_name)
                os.makedirs(processed_folder_path, exist_ok=True)

                # Recursively search for .java files in all variations of the folder
                for root, _, files in os.walk(folder_path):
                    for file in files:
                        if file.endswith(".java"):
                            try:
                                # Define new file name
                                new_file_name = f"{base_name}___{file}"
                                src_file_path = os.path.join(root, file)
                                dest_file_path = os.path.join(processed_folder_path, new_file_name)

                                # Copy the java file to the processed folder with the new name
                                shutil.copy(src_file_path, dest_file_path)
                            except Exception as e:
                                print(f"Error copying {file}: {e}")
            except Exception as e:
                print(f"Error processing folder {folder}: {e}")

        print("Java files successfully copied to PROCESSED folder.")

    except Exception as e:
        print(f"Error in main process: {e}")

# Run the processing function
process_folders()
