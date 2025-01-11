# The with keywword is used for context management. It ensures the special
# methods '__enter__' and '__exit__' are called on an object on entry and
# exit from the with statment respectively.

# Import module
import os

# Define MessageWriter class
class MessageWriter:
    # Constructor
    def __init__(self, file_name):
        self.file_name = file_name
    
    # Method called on entry to with statement
    def __enter__(self):
        self.file = open(self.file_name, 'w')
        return self.file

    # Method called on exit from the with statement
    def __exit__(self, *args):
        self.file.close()

# Using with statement with MessageWriter
curr_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(curr_dir, 'test_file.txt')
with MessageWriter(file_path) as file:
    file.write('hello world')