birthday = (4,15,2000)

print(len(birthday))

print(birthday[0])
print(birthday[1])
print(birthday[2])

# print(birthday[13])
# IndexError: tuple index out of range

print(birthday[-1])
print(birthday[-2])
print(birthday[-3])

# birthday[1] = 13
# TypeError: 'tuple' object does not support item assignment


addresses = (
    ["Hudson Street", "New York", "NY"],
    ["Palmer Street", "Cape Town", "WC"]
)

addresses[1][0] = "Polk Street"
print(addresses)


print(dir(birthday))