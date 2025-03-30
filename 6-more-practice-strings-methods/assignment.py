# Define a vowel_count function that accepts a string argument.
# The function should return the count of vowels in the string.
# You can assume the string will be in all lowercase.

def vowel_count(word):
    return word.count("a") +word.count("e")+word.count("i")+word.count("o")+word.count("u")
print(vowel_count("estate"))
print(vowel_count("helicopter"))
print(vowel_count("ssh"))


# Define a find_my_letter function that accepts two arguments: a string and a character.
# The function should return the first index position of the character in the string.
# It should return -1 if the character does not exist in the string.

def find_my_letter(string, char):
    return string.find(char)
print(find_my_letter("dangerous", "a"))
print(find_my_letter("bazooka", "z"))
print(find_my_letter("lollipop", "z"))