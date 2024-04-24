users = "user1"
password = "password1"

# TODO: Ask the user for their username and password
user_name = input("Enter your username: ")
user_password = input("Enter your password: ")

# TODO: Check if the entered username and password match any of the existing ones in the dictionary
# If they do, print a welcome message. If they don't, print an error message.
if user_name == users and user_password == password:
    print("Successful login!")
else:
    print("Username or password is incorrect")
    