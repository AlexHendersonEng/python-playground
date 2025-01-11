# Dictionary comprehension: Create dictionaries using an expression.
#                           dictionary = {key: expression for (key, value) in iterable}
#                           dictionary = {key: expression for (key, value) in iterable if condition}
#                           dictionary = {key: expression if condition else expression for (key, value) in iterable}

# Create list of keys and values for dictionary
keys = ['a', 'b', 'c', 'd', 'e']
values = [1, 2, 3, 4, 5]

# Create dictionary using dictionary comprehension
mydict = {key: value for (key, value) in zip(keys, values)}

# Print dictionary
print(mydict)

# Create dictionary using dictionary comprehension and if condition
mydict1 = {key: value for (key, value) in zip(keys, values) if key != 'c'}

# Print dictionary
print(mydict1)

# Create dictionary using dictionary comprehension and if/else condition
mydict2 = {key: (value if key != 'c' else 'Three') for (key, value) in zip(keys, values)}

# Print dictionary
print(mydict2)
