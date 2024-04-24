# Ask the user to choose one of two options:
# if they type 'p', our program should print "Hello" and then ask the user again. Keep repeating this until...
# if they type 'q', our program should terminate.

user_input = input("Type q or p: ")

while user_input == "p":
    print("Hello")
    user_input = input("Type q or p: ")
print("Program stopped")