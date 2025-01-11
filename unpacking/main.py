# Define list and dictionary
mylist = [1, 2, 3]
mydict = {"a" : 1,
          "b" : 2,
          "c" : 3}

# Define function
def print_items(a, b, c):
    print(a)
    print(b)
    print(c)

# Print items in list using unpacking
print_items(*mylist) # Equivalent to: print_items(1, 2, 3)

# Print items in dictionary using unpacking
print_items(**mydict) # Equivalent to: print_items(a=1, b=2, c=3)