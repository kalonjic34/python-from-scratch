# Define a function `add` that takes three arguments: a, b, and c
def add(a, b, c):
    print(f"The sum of three numbers is {a + b + c}")

# Call the function using positional arguments
add(5, 10, 15)

# Call the function using keyword arguments
add(a=5, b=10, c=15)

# Call the function using a mix of positional and keyword arguments
add(5, b=10, c=15)

# Call the function using a different order of keyword arguments
add(5, c=15, b=10)