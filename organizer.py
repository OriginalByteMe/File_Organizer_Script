# Python program to automatically organize
# Downloads folder in Python
 
# Import the libraries
from os import listdir
from os.path import isfile, join
import os
import shutil
 
# Define the file types to be organized
file_types = {
    'pdf': 'PDF_files',
    'doc': 'Word_files',
    'txt': 'Text_files',
    'png': 'Image_files',
    'jpg': 'Image_files',
    'jpeg': 'Image_files',
    'gif': 'Image_files',
    'mp3': 'Music_files',
    'mp4': 'Video_files',
    'zip': 'Compressed_files',
    'rar': 'Compressed_files',
    '7z': 'Compressed_files',
    'exe': 'Executable_files',
    'msi': 'Executable_files',
    'dmg': 'Executable_files',
    'ppt': 'Presentation_files',
    'pptx': 'Presentation_files',
    'xls': 'Excel_files',
    'xlsx': 'Excel_files',
    'csv': 'Excel_files',
    'html': 'HTML_files',
    'css': 'CSS_files',
    'js': 'JavaScript_files',
    'py': 'Python_files',
    'ipynb': 'Jupyter_Notebooks',
    'torrent': 'Torrent_files',
    'bin': 'Bin_files'
    
}

# Obtain the path to be organized 
file_path = "C:Downloads"  ## Replace with directory you wish to organize by file type
 
# Obtain all the files from the path in list
files = [f for f in listdir(file_path) if isfile(join(file_path, f))]
 
# Create the blank list and dictionary
file_list = []
filetype_dict = {}
 
# Create a loop
for file in files:
    if '.' not in file:
        continue
    # Get the extension of the file
    filetype = file.split('.')[-1]

    # Check if the file type exists in the list
    if filetype in file_types:
 
        # Add the file type in list if not already there
        if filetype not in file_list:
            file_list.append(filetype)
 
            # Give naming to the newly created folders
            new_folder_name = file_path+'/' + file_types[filetype]
 
            # Add the new folder name in dictionary with the key value pairs
            filetype_dict[filetype] = new_folder_name
 
            # Check if the folder exists or not
            if os.path.isdir(new_folder_name):
                # Come out of the loop if folder exists
                continue
            else:
                # Create the new folder if does not exist
                os.mkdir(new_folder_name)
 
# Declare a variable with value 1
i = 1
 
# Create the loop for all the files
for file in files:
 
    # Get the source path of each file
    src_path = file_path+'/'+file
 
    if '.' not in file:
            continue
    # Get the extension of the file
    filetype = file.split('.')[-1]
 
    # Check if the file type exists in the dictionary
    if filetype in filetype_dict:
 
        # Add the file type in dictionary if not already there
        dest_path = filetype_dict[filetype]
 
        # Move the file from source path to destination path
        shutil.move(src_path, dest_path)
 
    # Print from where to where a file is being moved
    print(i, '. ', src_path + '>>>' + dest_path)
 
    # Increment the value of variable by 1
    i += 1
