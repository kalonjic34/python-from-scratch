"""
This script calculates the total length of all command-line arguments passed to it.
It uses the sys module to access the arguments and iterates through them,
summing up their lengths to produce the final result.
"""

import sys

# print(sys.argv)
# print(type(sys.argv))

word_lengths = 0

for arg in sys.argv[1:]:
    word_lengths += len(arg)

print(f"the total length of all commanf line arguments is {word_lengths}")