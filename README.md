# Project README

## Project Overview

This project provides a set of Python scripts for handling compressed archives (ZIP, RAR, TAR.GZ, 7Z), extracting files, organizing Java files, and merging them into a structured folder. The main purpose is to process assignment submissions, particularly Java projects, by automatically unzipping archives, managing nested archives, and moving the relevant files into a final directory for further use or analysis.

### Features

- **Extracting Compressed Files:** Handles `.zip`, `.rar`, `.tar.gz`, and `.7z` files. Automatically renames and organizes files to avoid duplicates or malformed file names.
- **Nested Archive Handling:** The project can detect and extract nested archives recursively, ensuring no compressed file remains unprocessed within a parent archive.
- **Java File Merging:** Once all files are extracted, it processes the folders, finds all `.java` files, and moves them to a structured output folder, renaming them to avoid conflicts.

### Scripts

1. **`extracter.py`**
   - This script extracts files from archives (.zip, .rar, .tar.gz) located in the current working directory.
   - It creates an `EXTRACTED` folder to store the unzipped content.
   - The script handles malformed filenames (e.g., with extra extensions or spaces) and renames files to avoid naming conflicts.

2. **`nested_zip_remover.py`**
   - This script searches through the current working directory for archives (including nested ones) and extracts them recursively.
   - It supports `.zip`, `.rar`, `.tar.gz`, and `.7z` files.
   - The content is extracted into a folder named after the archive, without needing manual intervention.

3. **`merger.py`**
   - This script processes the `EXTRACTED` folder created by the `extracter.py` and `nested_zip_remover.py` scripts, looks for all `.java` files, and merges them into a new directory called `PROCESSED`.
   - Each `.java` file is renamed based on its source folder to avoid name conflicts generally created due to multiple turn-ins.
   - It handles multiple variations of the same submission by merging them into a common folder based on the base name.

### Usage

#### Prerequisites

- Python 3.x
- Required libraries:
  - `zipfile`, `tarfile`, `rarfile`, `py7zr`, `shutil`, `os`
  - Install `rarfile` using `pip install rarfile`
  - Install `py7zr` using `pip install py7zr`
  - Ensure `unrar.exe` is available for `.rar` extraction (set the path to this in the script).

#### Steps

1. **Extract the files**:
   - Run `extracter.py` to extract all archives in the working directory. The extracted files will be placed in the `EXTRACTED` folder.

   ```bash
   python extracter.py
   ```

2. **Handle Nested Archives**:
   - If the archives contain other compressed files, run `nested_zip_remover.py` to extract them recursively.

   ```bash
   python nested_zip_remover.py
   ```

3. **Merge Java Files**:
   - Once all archives are extracted, run `merger.py` to search for `.java` files and move them into the `PROCESSED` folder. Each file will be renamed according to the folder it came from to avoid conflicts.

   ```bash
   python merger.py
   ```

### Error Handling

- Each script logs errors during extraction, file renaming, or file copying. If errors occur (e.g., unsupported archive formats, missing files, etc.), they are printed to the console for easy debugging.
  
### Project Folder Structure

After running the scripts, the directory structure will look like this:

```
.
├── extracter.py
├── nested_zip_remover.py
├── merger.py
├── EXTRACTED/
│   ├── <ArchiveName1>/
│   ├── <ArchiveName2>/
│   └── ...
└── PROCESSED/
    ├── <BaseName1>/
    │   └── <BaseName1___FileName.java>
    ├── <BaseName2>/
    │   └── <BaseName2___FileName.java>
    └── ...
```
