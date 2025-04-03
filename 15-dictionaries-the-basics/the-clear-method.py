"""
This script demonstrates the use of the `clear` method and the `del` statement with dictionaries in Python.

1. A dictionary named `websites` is created with some key-value pairs.
2. The `clear` method is used to remove all items from the dictionary, leaving it empty.
3. The `del` statement is used to delete the dictionary entirely.
"""

websites ={
    "Wikipedia": "http://www.wikipedia.org",
    "Google": "http://www.google.com",
    "Netflix": "http://www.netflix.com",
}

websites.clear()
print(websites)

del websites
print(websites)