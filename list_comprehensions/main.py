# list comprehension: Create lists using an expression
#                     list = [expression for item in iterable]
#                     list = [expression for item in iterable if condition]
#                     list = [expression if condition else expression for item in iterable]

# Create list using list comprehension
squares = [i ** 2 for i in range(1, 11)]

# Print list
print("Squares:", squares, end="\n\n")

# Create list using list comprehension with if conditional
squares1 = [i ** 2 for i in range(1, 11) if i <= 5]

# Print list
print("Squares <= 5:", squares1, end="\n\n")

# Create list using list comprehension with if/else conditional
squares2 = [i ** 2 if i <= 5 else ">=5" for i in range(1, 11)]

# Print list
print("Squares >= 5:", squares2)

