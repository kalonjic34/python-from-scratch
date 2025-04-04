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


# Declare a common_elements function that accepts a dictionary.
# It should return a list with all of the elements that are found
# as both a key and a value in the dictionary.



my_dict = {
    "A":"K",
    "B":"D",
    "C":"A",
    "D":"Z"
}

def common_elements(my_dict):
    return [key for key in my_dict.keys() if key in my_dict.values()]

print(common_elements(my_dict))


# Assign a list of four dictionaries to a "complexity" variable below.

# The first and third dictionaries should have two key-value pairs.
# For those dictionaries, the keys should be strings and the values should be Booleans.

# The second and fourth dictionaries should have three key-value pairs.
# For those dictionaries, the keys should be floats and the values should be a list of strings.
# The lists can be of any length.

complexity = [
    {
        "A":True,    
        "B":False,    
    },
    {
        3.4: ["Apple","Orange"],
        6.7: ["Watermelon"],    
        10.2: ["Watermelon"]    
    },
    {
        "C":True,
        "D":False,
    },
    {
        3.4: ["Apple","Orange"],
        6.7: ["Watermelon"],    
        10.2: ["Watermelon"]   
    }
]

# Declare a plenty_of_arguments function that accepts two parameters (a and b)
# and an additional **kwargs parameter.
# The function should return True if the sum of a, b, and the values of
# **kwargs is greater than 100. It should return False otherwise.

def plenty_of_arguments(a,b,**kwargs):
    if a + b + sum(kwargs.values()) > 100:
        return True
    return False

print(plenty_of_arguments(20,30))
print(plenty_of_arguments(a = 50,b = 75))
print(plenty_of_arguments(a = 50,b = 75, c = 50))
print(plenty_of_arguments(a = 25,b = 25, c = 25, d = 25))

# Write a Python program to model a remote control feature for a television.
# Declare a stations_to_numbers function that accepts a dictionary.
# The keys will be the station names, and the values will be the channel numbers.

# EXAMPLE:
# channels = {'CBS': 2, 'NBC': 4, 'FOX': 5}
# stations_to_numbers(channels) => {'CBS': 2, 'NBC': 4, 'FOX': 5}

# The stations_to_numbers function should return a dictionary
# where the keys are the station names and the values are the channel numbers.

channels = {'CBS': 2, 'NBC': 4, 'FOX': 5}

def station_to_number(channels):
    return {station_number:channel_numbers for channel_numbers,station_number in channels.items()}

print(station_to_number(channels))

# Declare a coaster_conversion function that accepts a dictionary.
# The dictionary will have strings representing roller coasters as keys.
# The values will be the heights of each coaster in meters.

# Create a new dictionary with the same keys.
# The heights should be converted from meters to feet,
# and the result should be rounded to the closest integer.

# The round function rounds a number to the nearest integer.

# EXAMPLE:
# coasters = {'Kingda Ka': 138, 'Steel Vengeance': 130, 'Top Thrill Dragster': 126}
# coaster_conversion(coasters) => {'Kingda Ka': 456, 'Steel Vengeance': 427, 'Top Thrill Dragster': 413}

coasters = {'Kingda Ka': 138, 'Steel Vengeance': 130, 'Top Thrill Dragster': 126}
def coaster_converstion(coasters):
    return {coaster: round(meter * 3.28084) for coaster, meter in coasters.items()}
print(coaster_converstion(coasters))