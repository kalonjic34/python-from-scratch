# You have a list of friends' names. Write a loop to iterate over the list and print only the names that start with the letter 'J'.

friends = ["Rolf", "Jen", "Anne", "John"]

# TODO: Write a loop to iterate over the list and print only the names that start with 'J'.

for name in friends:
    if name[0] == "J":
        print(name)
