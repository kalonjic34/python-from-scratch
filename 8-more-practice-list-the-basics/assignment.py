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

# Define a split_in_two function that accepts a list and a number.
# If the number is even, return the list elements from the start of the list.
# If the number is odd, return the list elements from index 2 (inclusive) to 2 (exclusive).

def spilt_in_two(elements,number):
    if number % 2 == 0:
        return elements[2:]
    else:
        return elements[0:2]
        
elements = ["a", "b", "c", "d", "e", "f"]

print(spilt_in_two(elements,3))
print(spilt_in_two(elements,4))
print(spilt_in_two(elements,1))
print(spilt_in_two(elements,10))

# Declare a nested_extraction function that accepts a list of lists and an index number.
# The function should use the index as the basis of finding both the nested list
# and the element from that list with the given index position.
# You can assume the number of lists will always be equal to the number of elements given in each list.

def nested_extraction(nl,index):
    return nl[index][index]

nl = [[3, 4, 5], [7, 8, 9], [10, 11, 12]]

print(nested_extraction(nl, 0))
print(nested_extraction(nl, 1))
print(nested_extraction(nl, 2))

# Declare a beginning_and_end function that accepts a list of elements.
# It should return True if the first and last elements in the list
# are equal and False if they are unequal.
# Assume the list will always have at least 1 element.

def beginning_and_end(element):
    return element[0] == element[-1]

print(beginning_and_end([1,2,3,1]))
print(beginning_and_end([1,2,3,1,5]))
print(beginning_and_end(["a","b","c"]))
print(beginning_and_end([15]))

# Declare a long_word_in_collection function that accepts a list and a string.
# The function should return True if:
# - the word exists in the list AND
# - the word has more than 4 characters.


def long_word_in_collection(elements,target):
   return target in elements and len(target) > 4

elements = ["cat","dog","rhino"]
print(long_word_in_collection(elements,"rhino"))
print(long_word_in_collection(elements,"cat"))
print(long_word_in_collection(elements,"monkey"))

