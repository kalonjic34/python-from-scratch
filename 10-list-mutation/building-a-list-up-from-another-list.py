"""
This script demonstrates building new lists from an existing list using different transformations.

1. The `sqaures` function takes a list of numbers and returns a new list containing the squares of those numbers.
2. The `convert_to_floats` function takes a list of numbers and returns a new list where all numbers are converted to floats.
3. The `even_or_odd` function takes a list of numbers and returns a new list of booleans indicating whether each number is even (True) or odd (False).

The script uses the `powerball_numbers` list as input for these functions and prints the results.
"""

powerball_numbers = [4,8,15,16,23,42]

def sqaures(numbers):
    sqaures = []
    for number in numbers:
        sqaures.append(number ** 2)
    return sqaures

print(sqaures(powerball_numbers))

def convert_to_floats(numbers):
    floats = []
    for number in numbers:
        floats.append(float(number))
    return floats

print(convert_to_floats(powerball_numbers))

def even_or_odd(numbers):
    boolean = []
    for number in numbers:
        if number % 2 == 0:
            boolean.append(True)
        else:
            boolean.append(False)
    return boolean
print(even_or_odd(powerball_numbers))