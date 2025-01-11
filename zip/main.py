# The zip function takes two or more iterables and returns a zip object 
# which is an iterator of tuples where each item is an item from each of the
# iterables.

# Define two lists
numbers = [1, 2, 3, 4, 5]
letters = ['a', 'b', 'c', 'd', 'e']

# Iterate through the lists simultaneously using the zip function and print
for n, l in zip(numbers, letters):
    print("Number:", n, "Letter:", l)