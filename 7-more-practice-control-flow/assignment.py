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