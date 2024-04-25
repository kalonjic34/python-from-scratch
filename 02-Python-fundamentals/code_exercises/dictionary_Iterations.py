# Exercise 5: Destructuring in a Loop

# Given a list of friend tuples, print each friend's name and age.

friends = [("Rolf", 25), ("Anne", 37), ("Charlie", 31), ("Bob", 22)]

# TODO: Write a loop to iterate over the list and print each friend's name and age.

for name, age in friends:
    print(name, age)


# Exercise 6: Iterating over Dictionary Keys

# Given a dictionary of friend ages, print each friend's name.

friend_ages = {"Rolf": 25, "Anne": 37, "Charlie": 31, "Bob": 22}

# TODO: Write a loop to iterate over the dictionary keys and print each friend's name.

for name in friend_ages:
    print(name)


# Exercise 7: Iterating over Dictionary Values
# Given a dictionary of friend ages, print each friend's age.

friend_ages = {"Rolf": 25, "Anne": 37, "Charlie": 31, "Bob": 22}

# TODO: Write a loop to iterate over the dictionary values and print each friend's age.
for age in friend_ages.values():
    print(age)


# Exercise 8: Iterating over Dictionary Items
# Given a dictionary of friend ages, print each friend's name and age.

friend_ages = {"Rolf": 25, "Anne": 37, "Charlie": 31, "Bob": 22}

# TODO: Write a loop to iterate over the dictionary items and print each friend's name and age.

for name, age in friend_ages.items():
    print(name, age)