# File Organizer Script

## About
A Python script that organizes files in a chosen directory by their file extensions. It creates a folder for each extension type and moves matching files into it.

## Features
- Asks the user for a folder path
- Checks that the selected folder exists
- Identifies file extensions
- Creates destination folders automatically
- Moves files into the matching folders
- Places files without an extension in a `No Extension` folder

## Concepts Used
- File and directory operations with `os`
- Moving files with `shutil`
- Strings and file extensions
- Conditions and loops
- Basic path validation

## How to Run
Make sure Python is installed, open a terminal in this folder, and run:

```bash
python main.py
```

When prompted, enter the path to the folder you want to organize.

**Safety note:** Test the script on a temporary folder with sample files first. The script moves files from their original locations.

## TechNova Internship
Created for the TechNova Python Programming Internship to practice file and directory handling.
