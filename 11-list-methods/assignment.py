# Define an encrypt_message function that accepts a string.
# The input string will consist of only alphabetic characters.
# The function should return a string where all characters have been moved 
# "up" two spots in the alphabet. For example, "a" will become "c".

def encrypt_message(message):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
    encrypted = ""
    
    for letter in message:
        encrypted_letter_index_position = alphabet.index(letter) +2
        encrypted += alphabet[encrypted_letter_index_position]
        
    return encrypted

# print(encrypt_message("abc"))
# print(encrypt_message("xyz"))
# print(encrypt_message(""))

# Define a word_lengths function that accepts a string.
# It should return a list with the lengths of each word.

def word_lengths(string):
    words = string.split(" ")
    length = []
    for word in words:
        length.append(len(word))
    return length

print(word_lengths("Mary Poppins was a nanny"))
print(word_lengths("Somebody stole my donut"))

# Define a clean function that accepts a list of strings.
# It should return the strings joined together by a space.
# If some of the strings are empty or only consist of whitespace,
# they should not be included in the final string.

def cleanup(strings):
    clean_string = []
    
    for string in strings:
        if string.isspace() or len(string) == 0:
            continue
        clean_string.append(string)
    return " ".join(clean_string)
            
print(cleanup(["cat", "", "er", "pillar"]))
print(cleanup(["", " ", "pillow"]))