# Generators: A generator function returns an iterator object by using the yield
#             keyword to produce a series of results over time. This allows the 
#             function to generate values and pause its executioon after each yield,
#             maintaining its state between iterations.

# Define generator function
def counter(max):
    count = 1
    while count <= max:
        yield count
        count += 1

# Iterate over iterator returned from generator function
for n in counter(5):
    print(n)