try:
    # Try to execute the following code
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
    print("Result: ", result)
except ZeroDivisionError:
    # Handle division by zero exception
    print("Division by zero is not allowed")
except ValueError:
    # Handle invalid input exception
    print("Please enter a valid number")
except Exception as e:
    # Handle any other exception
    print("Some other exception occurred: ", e)
else:
    # Execute if no exception occurred
    print("No exception occurred")
finally:
    # Execute always
    print("This block will always execute")