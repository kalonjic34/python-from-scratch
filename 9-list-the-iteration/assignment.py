# Define a sum_of_lengths function that accepts a list of strings
# The function should return the sum of the string lengths

def sum_of_lengths(words):
    total = 0
    for word in words:
        total += len(word)
    return total
print(sum_of_lengths(["hello","Bob"]))
print(sum_of_lengths(["Nonsense"]))
print(sum_of_lengths(["Nonsense","or","confidence"]))

# Define a product function that accepts a list of numbers
# The function should return the product of the numbers
# The list will always have at least one value

def product(numbers):
    total_product = 1
    for number in numbers:
        total_product *= number
    return total_product
print(product([1,2,3]))      
print(product([4,5,6,7]))      
print(product([10]))      

# Define a smalllest_number function that accepts a list of numbers
# It should return the smallest value in the list

def smallest_number(numbers):
    lowest_number = numbers[0]
    for number in numbers:
        if number < lowest_number:
            lowest_number = number
    return lowest_number
print(smallest_number([1,2,3]))
print(smallest_number([3,2,1]))
print(smallest_number([4,5,4]))
print(smallest_number([-3,-2,-1]))

# Define a concatenate function that accepts a list of strings
# The functiion should return a concatenated string which consist of
# all list elements whose length is greater than 2 characters

def concatenate(words):
    sum_words = ""
    for word in words:
        if len(word) > 2:
            sum_words += word
    return sum_words
print(concatenate(["abc","def","ghi"]))
print(concatenate(["abc","de","fgh","gh"]))
print(concatenate(["ab","cd","ef","gh"]))

# Define a super_sum function that accepts a list of strings
# The function should sum the index positions of the first occurence of the letter "s" in each

def super_sum(word):
    total_char = 0
    for char in word:
        if "s" in char:
            index = char.index("s")
            total_char += index
    return total_char
print(super_sum([]))
print(super_sum(["mustache"]))
print(super_sum(["mustache","greatest"]))
print(super_sum(["mustache","pessimist"]))
print(super_sum(["mustache","pessimist","almost"]))

# Define in_list function that accepts a list of strings and a separate and separate string
# Return the index where the string exist in the list
# If the string does not exist, return -1


strings =["enchanted", "sparks fly", "long live"]

def in_list(strings,target):
    for index,element in enumerate(strings):
        if element == target:
            return index
    return -1

print(in_list(strings, "enchanted"))
print(in_list(strings, "sparks fly"))
print(in_list(strings, "fifteen"))
print(in_list(strings, "love story"))

#Define a sum_of_values_and_indices function that accepts a list of numbers
#It should return the sum of all elements along with along with index values

def sum_of_values_and_indices(numbers):
    total_sum = 0
    for index,number in enumerate(numbers):
        total_sum += index + number 
    return total_sum

print(sum_of_values_and_indices([1,2,3]))
print(sum_of_values_and_indices([0,0,0,0]))
print(sum_of_values_and_indices([0]))