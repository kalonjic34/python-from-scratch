# Define an odd function that accepts a single integer.
# If the integer is even, the function should return the string "even".
# If the integer is odd, the function should return the string "odd".

def even_or_odd(number):
    if number % 2 == 0:
        return "even"
    return "odd"
print(even_or_odd(2))
print(even_or_odd(0))
print(even_or_odd(13))
print(even_or_odd(9))

# Define a truth_or_falsy function that accepts a single argument.
# The function should return a string that reads "The value is truthy"
# if the argument is truthy, and "The value is falsy" otherwise.
# Ensure there is a space after "The value is" and before "truthy" or "falsy".

def truthy_or_falsy(value):
    if bool(value) > 0:
        return f"The value {value} is truthy"
    return f"The value {value} is falsy"
print(truthy_or_falsy(0))
print(truthy_or_falsy(5))
print(truthy_or_falsy("Hello"))
print(truthy_or_falsy(""))

# Declare a negative_energy function that accepts a numeric argument
# and returns its absolute value.
# The absolute value is the number's distance from zero.

def negative_energy(number):
    if number > 0:
        return number
    elif number < 0:
        return -1 * number
    else:
        return number
print(negative_energy(5))
print(negative_energy(10))
print(negative_energy(-5))
print(negative_energy(-8))
print(negative_energy(0))

# Define a divisible_by_three_and_four function that accepts a number as a
# parameter and returns True if the number is evenly divisible by both 3 and 4,
# and False otherwise.

def divisible_by_three_and_four(number):
    if number % 3 ==0 and number % 4 ==0:
        return True
    else:
        return False
print(divisible_by_three_and_four(3))
print(divisible_by_three_and_four(4))
print(divisible_by_three_and_four(12))
print(divisible_by_three_and_four(18))
print(divisible_by_three_and_four(24))

# Define a theory function that accepts a string as an argument.
# It should return True if the string has more than 3 characters
# and contains a capital "S". It should return False otherwise.


def string_theory(word):
    if len(word) > 3 and word.startswith("S"):
        return True
    else:
        print(False)
print(string_theory("Sansa"))
print(string_theory("Story"))
print(string_theory("See"))
print(string_theory("Fable"))