import random
"""
This demonstrates how to shuffle lists using Python's random module
It manipulates a list of character types and creates a shuffled copy
"""

characters = ["warrior", "druid","hunter","rogue","mage"]
print(random.shuffle(characters))
print(characters)

clone = characters[:]
clone = characters.copy()

random.shuffle(clone)
print(clone)