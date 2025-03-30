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