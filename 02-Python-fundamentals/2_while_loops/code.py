is_learning = True

while is_learning:
    print("You are learning!")
    user_input = input("Are you still learning? ")
    is_learning = user_input == "yes"
print("We stopped running")


user_input = input("Do you wished to run this program (yes/no)")

while user_input == "yes":
    print("We are running")
    user_input = input("Do you wished to run this program (yes/no)")

print("We stopped running")