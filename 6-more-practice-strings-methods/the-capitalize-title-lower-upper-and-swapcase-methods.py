"""
This script demonstrates the use of various string methods in Python:
- capitalize(): Capitalizes the first character of the string.
- title(): Converts the first character of each word to uppercase.
- upper(): Converts all characters to uppercase.
- lower(): Converts all characters to lowercase.
- swapcase(): Swaps the case of each character.
- Chaining methods: Combines multiple string methods for specific transformations.
"""

story = "once upon a time"

print(story.capitalize())
print(story.title())
print(story.upper())
print("HELLO".lower())
print("AbCdE".swapcase())
print("BENJAMIN FRANKLIN".lower().title())

print(story)

story = story.title()
print(story)