# The Python interpreter defines special variables in the form
# '__variable__' such as '__name__'.

# Import module
import module

# Print '__name__' variable of current module and imported module
print(__name__) # Prints: '__main__'
print(module.__name__) # Prints name of module: 'module'

# Use function in hello module
module.hello()