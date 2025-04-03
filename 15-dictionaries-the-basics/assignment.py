# Create an empty dictionary and assign it to the variable empty.
empty = {}

# Create a dictionary with three key-value pairs.
# The keys should be strings and the values should be integer values.
# Assign the dictionary to a my_dict variable.

my_dict = {
    "Chris": 25,
    "Dave": 20,
    "Debbie": 36
}

# A dictionary's keys can be any immutable data structure.
# Create a dictionary with two key-value pairs and assign it to
# a winning_lottery_numbers variable.
# Both of the keys should be tuples.
# One of the values should be True, the other value should be False.

winning_lottery_numbers = {
    (34,26,86,12,86): True,
    (23,88,43,21): False
}

# Define a to_dictionary function that accepts a list of strings.
# The function should return a dictionary where the keys are the strings
# and the values are their original index positions in the list.

detectives = ["Sherlock Holmes", "Hercule Poirot","Nancy Drew"]

def to_dictionary(elements):
    dict_list = {}
    for index, element in enumerate(elements):
        dict_list[element] = index
    return dict_list

print(to_dictionary(detectives))
            
# Define a length_counts function that accepts a list of strings.
# The function should return a dictionary where the keys represent
# length and the values represent how many strings have that length.

sa_countries = ["Brazil","Venezuela","Ecuador","Bolivia","Peru"]
            
def length_counts(elements):
    counts = {}
    for element in elements:
        length = len(element)
        current_count = counts.get(length,0)
        counts[length] = current_count +1
    return counts
print(length_counts(sa_countries))

# Declare a delete_keys function that accepts two arguments:
# a dictionary and a list of strings.
# For each string in the list, if the string exists as a dictionary key,
# delete the key-value pair from the dictionary.
# If the string does not exist as a dictionary key, avoid an error.
# The return value should be the modified dictionary object.

my_dict = {'A': 1, 'B': 2, 'C': 3}
strings = ["A", "C"]

def delete_keys(my_dict, strings):
    for string in strings:
        if string == my_dict:
            my_dict.pop(string)
    return my_dict

print(delete_keys(my_dict, strings))