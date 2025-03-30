"""
This script demonstrates the usage of the `startswith()` and `endswith()` string methods in Python
- The `startswith()` method checks if a string starts with a specified prefix
- The `endswith()` method checks if a string ends with a specified suffix
The script uses the `salutation` variable, which contains the string "Mr. Kermit the Frog", 
to perform various checks with both methods. It includes examples with exact matches, 
case sensitivity, and partial matches to illustrate how these methods behave
    Note:
- The examples show how `startswith()` and `endswith()` are case-sensitive
- The script includes both successful and unsuccessful checks to highlight the behavior of these methods

"""

salutation = "Mr. Kermit the Frog"

print(salutation.startswith("M"))
print(salutation.startswith("Mr"))
print(salutation.startswith("Mr."))
print(salutation.startswith("m"))
print(salutation.startswith("mr."))
print(salutation.startswith("Ker"))
print(salutation.startswith("Mr. Ker"))

print()

print(salutation.endswith("g"))
print(salutation.endswith("og"))
print(salutation.endswith("Frog"))
print(salutation.endswith("frog"))