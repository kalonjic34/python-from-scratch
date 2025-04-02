"""
This script demonstrates the use of Python's built-in `filter` and `map` functions with lambda expressions

1. The `filter` function is used to filter elements from the `metals` list based on specific conditions:
    - The first `filter` checks for metals with names longer than 5 characters
    - The second `filter` does the same but uses a different lambda variable name
    - The third `filter` checks for metals whose names start with the letter "p"

2. The `map` function is used to apply transformations to each element in the `metals` list:
    - The first `map` counts the occurrences of the letter "l" in each metal name
    - The second `map` replaces the letter "s" with the dollar sign "$" in each metal name
"""

metals = ["gold","silver","platinum","palladium"]

print(list(filter(lambda metal: len(metal) > 5,metals)))
print(list(filter(lambda element: len(element) > 5,metals)))
print(list(filter(lambda word: word.startswith("p"), metals)))

print(list(map(lambda word: word.count("l"),metals)))
print(list(map(lambda word: word.replace("s", "$"),metals)))