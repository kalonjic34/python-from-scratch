friends_ages = {"James": 25, "Sam": 26, "Ian": 27, "Rob": 23}

# for name in friends_ages.values():
#     print(name)

for name, age in friends_ages.items():
    print(f"{name} is {age} years old")