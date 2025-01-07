# Define variables
var1 = "cow"
var2 = "moon"
var3 = 156823.23456789

# Format string using format method
print("The {} jumps over the {}".format(var1, var2))
print("The {0} jumps over the {1}".format(var1, var2))
print("The {str1} jumps over the {str2}".format(str1=var1, str2=var2))
print(f"The {var1} jumps over the {var2}")

# Use modifiers in string formatting
print(f"Account balance: {var3:.2f}") # 2 decimal places
print(f"Account balance: {var3:e}") # scientific notation
print(f"Account balance: {var3:,}") # comma separator
