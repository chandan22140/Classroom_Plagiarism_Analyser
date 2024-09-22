import os

# Define the base directory
base_dir = './PROCESSED'

# Traverse the base directory recursively
for root, dirs, files in os.walk(base_dir):
    # Filter out Java files in the current directory
    java_files = [file for file in files if file.endswith('.java')]
    
    # If there's more than one Java file, merge them
    if len(java_files) > 1:
        merged_file_path = os.path.join(root, 'merged_file.java')
        
        with open(merged_file_path, 'w') as merged_file:
            # Iterate through all Java files in the subdirectory
            for java_file in java_files:
                java_file_path = os.path.join(root, java_file)
                
                with open(java_file_path, 'r') as file:
                    # Write the content of each Java file to the merged file
                    merged_file.write(f"// Start of {java_file}\n")
                    merged_file.write(file.read())
                    merged_file.write(f"\n// End of {java_file}\n\n")
                
                # Optionally delete the original file after merging
                os.remove(java_file_path)
        
        print(f"Merged {len(java_files)} Java files into: {merged_file_path}")
    elif len(java_files) == 1:
        print(f"Subdirectory {root} has only one Java file. No merge needed.")
    else:
        print(f"Subdirectory {root} has no Java files.")

# Traverse the base directory recursively
for root, dirs, files in os.walk(base_dir):
    # Filter out Java files in the current directory
    java_files = [file for file in files if file.endswith('.java')]
    
    # If there's more than one Java file, merge them
    if len(java_files) > 1:
        # Get the subdirectory name
        subdir_name = os.path.basename(root)
        merged_file_path = os.path.join(root, f'{subdir_name}.java')

        try:
            with open(merged_file_path, 'w', encoding='utf-8') as merged_file:
                # Iterate through all Java files in the subdirectory
                for java_file in java_files:
                    java_file_path = os.path.join(root, java_file)
                    
                    try:
                        with open(java_file_path, 'r', encoding='utf-8') as file:
                            # Write the content of each Java file to the merged file
                            merged_file.write(f"// Start of {java_file}\n")
                            merged_file.write(file.read())
                            merged_file.write(f"\n// End of {java_file}\n\n")
                    except Exception as file_error:
                        print(f"Error reading {java_file_path}: {file_error}")
                        continue
                    
                    # Optionally delete the original file after merging
                    os.remove(java_file_path)

            print(f"Merged {len(java_files)} Java files into: {merged_file_path}")

        except Exception as merge_error:
            print(f"Error merging files in {root}: {merge_error}")

    elif len(java_files) == 1:
        print(f"Subdirectory {root} has only one Java file. No merge needed.")
    else:
        print(f"Subdirectory {root} has no Java files.")
