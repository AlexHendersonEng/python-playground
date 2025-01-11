# A global variable can be created and modified inside a function
# using the global keyword

# Define function which defines global variable
def func():
  global x
  x = "Global variable"

# Call function
func()

# Print global variable
print("Variable: " + x)