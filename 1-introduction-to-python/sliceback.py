letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# backwards = letters[25::-1]
backwards = letters[::-1]
print(backwards)

# Create a slice that produces the character qpo
print(letters[16:13:-1])

# Slice the string to produce edcba
print(letters[4::-1])

# Slice the string to produce the last 8 characters, in reverse order
print(letters[:-9:-1])

print(letters[-4:])
print(letters[-1:])
print(letters[:1])
print(letters[0])