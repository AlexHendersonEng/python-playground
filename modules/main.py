# A module is a file containing Python code. Modules can define
# functions, classes, and variables. They can also be imported
# into a python file in varying ways as demonstrated below.
#    - Import entire module using default namespace: import <module_name>
#    - Import specific functions from a module: from <module_name> import <function_name1>, <function_name2>
#    - Import all functions from a module: from <module_name> import *
#    - Import a module with an alias: import <module_name> as <alias>
#
# When importing modules a __pycache__ directory is created to store a
# bytecode compiled version of the module. This speeds up the loading
# of the module next time it is imported. This will be recreated when
# the module is modified.

# Import the messages module
from messages import *

# Call message module methods
hello()
bye()

# List modules that are available in the Python environment
help('modules')