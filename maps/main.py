# The map function applies a function each item in an iterable

# Generic store data 
store = [("shirt", 20.0), 
         ("trousers", 30.0),
         ("jacket", 50.0),
         ("socks", 5.0)]

# Increase pices by 10% by using map
new_store = list(map(lambda listing : (listing[0], listing[1] * 1.1), store))

# Print
print("Original prices:")
print(store, end="\n\n")
print("Increased prices:")
print(new_store)