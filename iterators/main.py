# Iterator: An object which implements the iterator protocol, which consists
#           of the methods '__iter__()' and '__next__()'. This allows the 
#           object to be iterated through. A for loop implicitly calls the 
#           iter function and then iterates through the object using the next
#           function.

# Define an iterator object
class MyWords:

    # Constructor method
    def __init__(self, words):
        self.words = words

    # Iterator method which initialises iterator and returns object
    def __iter__(self):
        self.idx = 0
        return self

    # Next method which returns the next item
    def __next__(self):
        # If index out of bounds raise StopIteration error
        if self.idx > len(self.words) - 1:
            raise StopIteration

        # Return word at current index and increment index
        x = self.words[self.idx]
        self.idx += 1
        return x

# The list object has an iterator
print("List object iterator:")
mylist = ["One", "Two", "Three"]
myiter = iter(mylist) # Construct iterator explicitly
print(next(myiter)) # Call next function explictly
print(next(myiter)) # Call next function explictly
print(next(myiter)) # Call next function explictly
print("")

# Construct custom iterator object
print("Custom object iterator:")
mywords = MyWords(["One", "Two", "Three"])
for word in mywords: # Use iterator implictly
    print(word)
print("")


