# Given the great_directors list below, overwrite the "Steven Spielberg" 
# entry with a string of "Michael Bay".

great_directors = ["Martin Scorsese", "Steven Spielberg","Francis Ford Coppola"]
great_directors[1] = "Michael Bay"
print(great_directors)

# Given the transformers list below, overwrite "Bumblebee" with "Grimlock".
transformers = ["Optimus Prime", "Megatron", "Bumblebee", "Starscream"]
transformers[2] = "Grimlock"
print(transformers)

# Given the camping_trip_supplies list below, overwrite "Socks" with "Food".
camping_trip_supplies = ["Socks","Flashlight", "Tent", "Blanket"]
camping_trip_supplies[0] ="Food"
print(camping_trip_supplies)

# Given the tech_companies list below, overwrite the Microsoft, Blackberry, 
# and IBM strings with the strings "Facebook" and "Apple". Use list slicing syntax.

tech_companies = ["Google", "Microsoft","Blackberry","IBM","Yahoo"]
tech_companies[1:4] = "Facebook","Apple"
print(tech_companies)


# Declare a length_match function that accepts a list of strings and an integer.
# It should return a count of the number of strings whose length is equal to the number.

def length_match(values, target):
    count = 0
    for value in values:
        if len(value) == target:
            count += 1
            
    return count
print(length_match(["dog", "kangaroo", "mouse"], 3))
print(length_match(["cat", "dog", "kangaroo", "mouse"], 3)) 

# Declare a sum_from function that accepts two numbers as arguments.
# The second number will always be greater than the first number.
# The function should return the sum of all numbers from the first number to the second number (inclusive).

def sum_from(start, end):
    total_sum = 0
    for number in range(start,end +1):
        total_sum += number
    return total_sum

print(sum_from(1, 5)) 
print(sum_from(3, 7)) 
print(sum_from(6, 12))

# Declare a same_index_values function that accepts two lists.
# The function should return a list of the index positions 
# in which the two lists have equal elements.

def same_index_values(list1, list2):
    results = []
    
    for index, value in enumerate(list1):
        if value == list2[index]:
            results.append(index)
    return results

print(same_index_values([1, 2, 3], [3, 2, 1]))
print(same_index_values(["a", "b", "c"], ["c", "b", "d"]))

# Define an evens function that accepts a list of numbers.
# The function should return a new list consisting of only the even numbers from the original list.

numbers_list = [4,8,15,16,23,42]

def only_evens(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

print(only_evens(numbers_list))

# Define a long_strings function that accepts a list of strings.
# The function should return a new list consisting of only the strings with 5 characters or more.

def long_strings(strings):
    string_list = []
    for string in strings:
        if len(string) >= 5:
            string_list.append(string)
    return string_list

print(long_strings(["Hello", "Goodbye", "Saw"]))
print(long_strings(["a", "cat", "Job"]))

# Write a factors function that accepts a positive whole number.
# It should return a list of all of the number's factors in ascending order.
# HINT: Could the range function be helpful here? Or maybe a while loop?

def factors(number):
    factor_numbers = []
    for i in range(1, number + 1):
        if number % i == 0:
            factor_numbers.append(i)
    return factor_numbers

print(factors(1))
print(factors(2))
print(factors(10))
print(factors(64))

# Declare a delete_all function that accepts a list of strings and a target string.
# Remove all occurrences of the target string from the list and return it.

def delete_all(items, target):
    while target in items:
        items.remove(target)
    return items

print(delete_all([1,3,5], 5))
print(delete_all(["x", "y", "z", "x", "x"], "x"))
print(delete_all(["apple", "banana", "apple", "cherry"], "apple"))

# Declare a push_or_pop function that accepts a list of numbers.
# Build up and return a new list by iterating over the list of numbers.
# If a number is greater than 5, add it to the end of the new list.
# If a number is less than or equal to 5, remove the last element added to the new list.

def push_or_pop(numbers):
    numbers_list = []
    for number in numbers:
        if number > 5:
            numbers_list.append(number)
        elif number <= 5:
            numbers_list.pop()
    return numbers_list

print(push_or_pop([10]))
print(push_or_pop([10,4]))
print(push_or_pop([10,20,30]))
print(push_or_pop([10,30]))