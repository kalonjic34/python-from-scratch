"""
This script demonstrates the use of various boolean string methods in Python.
Each method checks a specific property of the string and returns True or False.
"""

print("winter".islower())
print("winter 12#".islower())
print("Winter 12#".islower())

print("SUMMER".isupper())
print("SUMMER 34%#".isupper())
print("sUMMER 34%#".isupper())

print("The Four Seasons".istitle())
print("The 4 Seasons".istitle())
print("The four Seasons".istitle())

print("Area".isalpha())
print("Area 51".isalpha())

print("51".isnumeric())
print("Area 51".isnumeric())

print("Area51".isalnum())
print("Area 51".isalnum())

print(" ".isspace())
print(" k ".isspace())
print(" 4 ".isspace())
print(" ! ".isspace())