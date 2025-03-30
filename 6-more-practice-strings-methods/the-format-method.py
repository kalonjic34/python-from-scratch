# name, adjective, noun
# mad_libs = "{} laughed at the {} {}."

# print(mad_libs.format("Robby","green", "alien"))
# print(mad_libs.format("Sam","silly", "tomato"))

# print(mad_libs.format("Sam","silly", ))
# IndexError: Replacement index 2 out of range for positional args tuple

# mad_libs = "{2} laughed at the {1} {0}."

# print(mad_libs.format("Robby","green", "alien"))
# print(mad_libs.format("Sam","silly", "tomato"))

mad_libs = "{name} laughed at the {adjective} {noun}."

# print(mad_libs.format(name="Robby",adjective="green", noun="alien"))
# print(mad_libs.format(name="Sam",adjective="silly", noun="tomato"))
# print(mad_libs.format(adjective="silly", noun="tomato",name="Sam"))

name = input('Enter a name: ')
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")

print(mad_libs.format(name = name, adjective = adjective, noun = noun))