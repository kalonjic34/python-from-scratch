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