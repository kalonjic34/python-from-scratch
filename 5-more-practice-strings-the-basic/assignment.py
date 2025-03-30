# Define a long_word function that accepts a string.
# The function should return a Boolean that reflects
# whether the string has more than 7 characters.

def long_word(word):
    return len(word) > 7
print(long_word("Python"))
print(long_word("magnificent"))

# Define a first_longer_than_second function that accepts two strings.
# The function should return a True if the first string is longer than the second string, and False otherwise (including if they are equal in length).

def first_longer_than_second(first_word, second_word):
    return len(first_word) > len(second_word)
print(first_longer_than_second("Python", "Ruby"))
print(first_longer_than_second("cat", "mouse"))
print(first_longer_than_second("Steven", "Seagal"))

# Define a first_and_last_letter function that accepts a string as an argument
# input and should return True if the first and last character are equal.

def same_first_and_last_letter(word):
    return word[0] == word[-1]
print(same_first_and_last_letter("runner"))
print(same_first_and_last_letter("Runner"))
print(same_first_and_last_letter("clock"))
print(same_first_and_last_letter("q"))

# Define a three_number_sum function that accepts a 3-character string as an argument.
# The function should add up the sum of the digits of the string.
# You’ll need to figure out a way to convert the stringified number.

def three_number_sum(wordsum):
    return int(wordsum[0]) + int(wordsum[1]) + int(wordsum[2])
print(three_number_sum("123"))
print(three_number_sum("567"))
print(three_number_sum("444"))
print(three_number_sum("000"))

# Define a first_three_characters function that accepts a string argument.
# The function should return the first 3 characters of the string.

def first_three_characters(char):
    return char[0:3]
print(first_three_characters("dynasty"))
print(first_three_characters("empire"))

# Define a last_five_characters function that accepts a string argument.
# The function should return the last 5 characters of the string.

def last_five_characters(char):
    return char[-5:]
print(last_five_characters("dynasty"))
print(last_five_characters("empire"))

# Define a is_palindrome function that accepts a string argument.
# The function should return True if the string is spelled the same backwards as it is forwards.
# Return False otherwise.

def is_palindrome(word):
    return word[:] == word[::-1]

print(is_palindrome("racecar"))
print(is_palindrome("yummy"))