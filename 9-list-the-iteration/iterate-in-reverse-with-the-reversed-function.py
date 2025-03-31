"""
This script demonstrates two ways to iterate over a list in reverse order.
1. Using slicing with [::-1].
2. Using the built-in reversed() function.
"""

the_simpsons = ["Homer", "Marge","Bart","Lisa","Maggie"]

for character in the_simpsons[::-1]:
    print(f"{character} has a total of {len(character)} characters")

print(reversed(the_simpsons))
print(type(reversed(the_simpsons)))

for character in reversed(the_simpsons):
    print(f"{character} has a total of {len(character)} characters")

    