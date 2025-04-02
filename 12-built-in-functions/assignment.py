# Declare a right_words function that accepts a list of words and a number.
# Return a new list with the words that have a length equal to the number.

def right_word(words, number):
    return list(filter(lambda word: len(word) == number,words))

print(right_word(["cat", "dog", "bean", "ace", "heart"], 3))
print(right_word(["cat", "dog", "bean", "ace", "heart"], 5))
print(right_word([],4))

# Declare an only_odds function.
# It should accept a list of whole numbers.
# It should return a list with the odd numbers from the original list.
# Do NOT use list comprehension.

def only_odds(numbers):
    return list(filter(lambda number: number % 2 == 1,numbers))

print(only_odds([1, 3, 5, 6, 7, 8]))
print(only_odds([2, 4, 6]))

# Declare a count_of_a function that accepts a list of strings.
# It should return a list with counts of how many "a" characters appear per string.

def count_of_a(strings):
    return list(map(lambda string: string.count("a"),strings))

print(count_of_a(["alligator", "aardvark", "albatross"]))
print(count_of_a(["apple", "banana", "grape"]))

# Define a greater_sum function that accepts two lists of numbers.
# Return the list with the greatest sum.
# It is guaranteed that the lists will always have different sums.

def greater_sum(l1,l2):
    if sum(l1) > sum(l2):
        return l1
    return l2

print(greater_sum([1, 2, 3], [2, 4]))
print(greater_sum([1, 2, 3, 4], [1, 2]))

# Define a sum_difference function that accepts two lists of numbers.
# It should return the difference between the sum of values in the first list
# and the sum of values in the second list.

def sum_difference(l1, l2):
    return sum(l1) - sum(l2)

print(sum_difference([1, 2, 3], [1,2, 4]))
print(sum_difference([1, 2, 3, 4], [1, 2]))
print(sum_difference([1], [1]))