age = 24

print(f"You are {age}")

name = "Chris"
# greetings = f"How are you, {name}?"
# print(greetings)

# name = "Liam"
# print(greetings)


final_greeting = "How are you, {}?"

chris_greeting = final_greeting.format(name)
print(chris_greeting)

liam_greeting = final_greeting.format("Liam")
print(liam_greeting)


