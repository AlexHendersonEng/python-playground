# A package is a way to structure code into reusable components
# using directories. Packages contain modules which can define
# functions, classes, and variables that can be imported.
# 
# Adding an '__init__.py' file to a directory tells Python
# that the directory should be treated as a package and can be used to run 
# initialisation code. Subpackages can also be added by adding subdirectories
# with their own respective '__init__.py' files.
#
# To distribute a package a 'setup.py' file can be used along with the setuptools
# library. This file defines metadata about the package and specifies how it
# should be installed.
#
# When importing packages/modules a __pycache__ directory is created to store a
# bytecode compiled version of the package/module. This speeds up the loading of the
# package/module next time it is imported. This will be recreated when the
# package/module is modified.

# Import functions from packages
from mypackage.hello_module import hello
from mypackage.mysubpackage.bye_module import bye

# Call imported functions
hello()
bye()