# You have a list of items that you need to buy from the grocery store
shopping_list = ["milk", "bread", "eggs", "butter", "cheese"]

# TODO: Ask the user to enter an item
user = input("Enter an item from the shopping list: ")

# TODO: Check if the item is already in the shopping list
# If it is, print a message saying the item is already in the list
# If it's not, add the item to the list and print a message saying it was added

if user == shopping_list[:]:
    print("The item is already in the list")
else:
    shopping_list.append(user)
    print(f"Item '{user}' is added!")
    print(shopping_list)