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

# Define a first_and_last function that accepts a list of strings.
# The function should return a concatenation of the first and the last element.


def first_and_last(concat_elements):
    return concat_elements[0] + concat_elements[-1]
    
print(first_and_last(["a","b","c"]))
print(first_and_last(["bob","tom","rob"]))
print(first_and_last(["a"]))

# Define a product_of_even_indices function that accepts a list of numbers.
# The list will always have 6 total elements.
# It should return the product of the numbers at even indices.

def product_of_even_indices(numbers):
    return numbers[0] * numbers[2] * numbers[4]

print(product_of_even_indices([1,2,3,4,5,6]))
print(product_of_even_indices([3,4,3,5,3,6]))

# Define a first_letter_of_last_string function that accepts a list of strings.
# It should return one character—the first letter of the last string in the list.
# The list will always have at least one string.

def first_letter_of_last_string(elements):
    return elements[-1][0]

print(first_letter_of_last_string(["cat","dog","zebra"]))
print(first_letter_of_last_string(["nonsense"]))