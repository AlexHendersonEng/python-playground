# The filter function creates a collection of elements from an iterable for which a
# function returns true

# Create list of friends with ages
friends = [("Bob", 20),
           ("Fred", 16),
           ("Tom", 18),
           ("Ted", 19),
           ("Alfie", 17)]

# Use filter function to get friends 18 or over
new_friends = list(filter(lambda friend : friend[1] >= 18, friends))

# Print friends 18 or over
print("Friends:")
print(friends, end="\n\n")
print("Friends 18 or over:")
print(new_friends)