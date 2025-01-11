# The reduce function applies a functiuon to an iterable and reduces it to a single
# cumulative value. It does this by performing a function on the first two elements
# and repeating this until 1 value remains

# Import functools module
import functools

# Define list
letters = ["H", "E", "L", "L", "O"]

# Reduce list to one value
word = functools.reduce(lambda l1, l2 : l1 + l2, letters)

# Print value
print(word)