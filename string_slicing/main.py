# Define string for slicing
message = "Hello, World!"
print("Original message: ", message, "\n")

# Slice the string using indexing [start:stop:step]
print("String slicing using indexing:")
print("First word: ", message[:5]) # [0:5]
print("Second word: ", message[7:]) # [7:end]
print("Step of two: ", message[::2]) # [0:end:2]
print("Reversed message: ", message[::-1], "\n") # [0:end:-1]

# Slice the string using slice object
print("String slicing using slice object:")
slice_obj = slice(0, 5)
print("First word: ", message[slice_obj]) # [0:5]

