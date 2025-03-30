"""
This script demonstrates the usage of the `find` and `index` string methods in Python.
- The `find` method is used to locate the first occurrence of a substring in a string.
    It returns the index of the first occurrence or `-1` if the substring is not found.
- The `index` method is similar to `find`, but it raises a `ValueError` if the substring is not found
    Note:
- The script includes examples of both successful and unsuccessful searches using `find` and `index`
- The last line demonstrates the exception raised by `index` when the substring is not found
"""

browser = "Google Chrome"

print(browser.find("C"))
print(browser.find("Ch"))
print(browser.find("o"))
print(browser.find("G"))
print(browser.find("z"))
print(browser.find("zxy"))
print(browser.find("c"))

print()

print(browser.find("o"))
print(browser.find("o",2))
print(browser.find("o",5))

print("Ch" in browser)

print(browser.index("C"))

# print(browser.index("Z"))
# ValueError: substring not found