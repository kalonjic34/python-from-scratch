def word_multiplier(word: str, times: int) -> str:
    return word * times

"""
This script demonstrates the use of function annotations in Python.
The `word_multiplier` function takes a string and an integer as input,
and returns the string repeated the specified number of times.

The first `print` statement calls the function with valid arguments.
The second `print` statement demonstrates what happens when invalid arguments are passed.
"""

print(word_multiplier("dog",5))
print(word_multiplier(10,5))