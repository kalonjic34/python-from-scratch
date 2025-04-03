# Declare an invert function that accepts a dictionary object.
# The function should return a new dictionary where the keys and values from the original dictionary are inverted.
# Each value should be a key, and each value of the original dictionary should be a value.
# Ensure both the keys and values of the dictionary are immutable.

my_dict = {'A': 'B', 'C': 'D', 'E': 'F'}

def invert_function(my_dict):
    new_dict = {}
    for key,value in my_dict.items():
        new_dict[value] = key
    return new_dict

print(invert_function(my_dict))

# Declare a count_of_value function that accepts a dictionary and an integer.
# It should return a count of the number of times the integer appears as a value among the dictionary's values.

my_dict1 = {'a': 1, 'b': 3, 'c': 5}

def count_of_value(dictionary, value):
    count = 0
    for k,v in dictionary.items():
        if v == value:
            count +=1
    return count

print(count_of_value(my_dict1, 1))
print(count_of_value(my_dict1, 5))
print(count_of_value(my_dict1, 3))

# Declare a sum_of_values that accepts a dictionary and a list of strings.
# The dictionary will have keys of strings and values of numbers.
# The function should return the sum of values for dictionary keys that are also found in the list.

# NOTE: sum is a reserved keyword in Python. Don't use it as a variable name.
my_dict = {'a': 5, 'b': 3, 'c': 10}
def sum_of_values(dictionary1, keys):
    total = 0 
    
    for k,v in dictionary1.items():
        if k == keys:
            total += v
    return total

print(sum_of_values(my_dict, ["a"]))
print(sum_of_values(my_dict, ["a", "c"]))
print(sum_of_values(my_dict, ["b", "a", "c"]))