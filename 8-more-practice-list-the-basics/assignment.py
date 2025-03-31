empty = []

 # Create a list with a single Boolean - True - and assign it to the variable "empty".

active = [True]

# Create a list with 6 integers of your choice and assign it to the variable "favorite_numbers".

favorite_numbers = [8,34,10,77,12,33]

# Create a list with 3 strings - "red", "green", "blue" - and assign it to the variable "colors".

colors = ["red", "green", "blue"]

# Define a long function that accepts a single list as an argument.
# It should return True if the list has more than 5 elements, and False otherwise.

def is_long(elements):
    if len(elements) > 5:
        return True
    else:
        return False
       
print(is_long(empty))
print(is_long(active))
print(is_long(favorite_numbers))
print(is_long(colors))