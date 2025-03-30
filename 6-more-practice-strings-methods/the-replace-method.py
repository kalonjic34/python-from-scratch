"""
This script demonstrates the use of the `replace` method in Python
It starts with a phone number string and performs the following operations:
1. Replaces spaces with hyphens
2. Replaces the digit '4' with '3'
3. Shows that the original string remains unchanged after the `replace` method
4. Updates the phone number variable by replacing spaces with hyphens and prints the updated value
"""

phone_number = "071 446 7780"
print(phone_number.replace(" ", "-"))
print(phone_number.replace("4", "3"))

print(phone_number)

phone_number = phone_number.replace(" ", "-")
print(phone_number)