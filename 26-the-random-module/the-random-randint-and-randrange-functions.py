import random
""" 
This script demonstrates various ways to generate random numbers in Python 
using the 'random' module.
"""

# Generates a random float between 0 and 1, then multiplies by 100 to scale it up
print(random.random() * 100)

# Generates a random float between 0 and 1, then multiplies by 100 to scale it up
print(random.randint(1, 5))

# Generates a random number from the range 0 to 50 with a step of 10 (e.g., 0, 10, 20, 30, 40)
print(random.randrange(0,50,10))