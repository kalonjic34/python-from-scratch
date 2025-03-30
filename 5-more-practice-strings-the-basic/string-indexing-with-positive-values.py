"""
This script demonstrates string indexing with positive values in Python
It uses the string "Python" and accesses individual characters using their indices
It also shows the immutability of strings and the behavior of out-of-range indices
"""

best_language_ever = "Python"

print(best_language_ever[0])
print(type(best_language_ever[0]))

print(best_language_ever[1])
print(best_language_ever[3])
print(best_language_ever[2 * 2])

print(len(best_language_ever))
print(best_language_ever[5])

# print(best_language_ever[100]) 
# IndexError: string index out of range

# best_language_ever[0] = "B"
# TypeError: 'str' object does not support item assignment
