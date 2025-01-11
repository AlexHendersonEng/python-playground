# Define function
def hello():
    print("Hello")

# Use '__name__' special variable to determine whether module is
# being run directly or imported
if __name__ == "__main__":
    print("module is being run directly")
else:
    print("module is being imported")

