# Import modules
import os
import sys
import shutil

# Define path to file
file_dir = os.path.dirname(os.path.abspath(__file__))
test_file_path = os.path.join(file_dir, 'test.txt')
print(f'File path: {test_file_path}')

# Write to file
with open(test_file_path, 'w') as file:
    file.write('Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nulla magnam non ducimus' +
               'repellat voluptatibus iure asperiores sequi assumenda nobis placeat atque temporibus' +
               'excepturi molestias, illo exercitationem doloremque quas quidem rem?')
    print('File written')

# Check if file exists
if os.path.exists(test_file_path):
    print('File exists')

    # Check if file is a file or directory
    if os.path.isfile(test_file_path):
        print('File is a file')
    elif os.path.isdir(test_file_path):
        print('File is a directory')
else:
    print('File does not exist')
    sys.exit()

# Read file content and print it
with open(test_file_path, 'r') as file:
    print('File contents: ' + file.read())

# Copy file
file_copy_path = os.path.join(file_dir, 'test_copy.txt')
shutil.copy(test_file_path, file_copy_path)
print(f'File copied to: {file_copy_path}')

# Create new directory
new_dir_path = os.path.join(file_dir, 'new_dir')
os.mkdir(new_dir_path)
print(f'New directory created: {new_dir_path}')

# Move file to new directory
shutil.move(file_copy_path, new_dir_path)
print(f'File moved to: {new_dir_path}')

# Delete generated directories and files
os.remove(test_file_path)
os.remove(os.path.join(new_dir_path, 'test_copy.txt'))
os.rmdir(new_dir_path)
print('Files and directories deleted')