"""
# Initially, the variable `a` is assigned the integer value 3.
# Then, `a` is reassigned to the integer value 10, making the previous value (3) eligible for garbage collection.
# Next, `a` is reassigned to the string "hello", making the previous value (10) eligible for garbage collection.
# After that, `a` is reassigned to a list [1,2,3], making the previous value ("hello") eligible for garbage collection.
# Finally, `a` is reassigned to another list [4,5,6], making the previous list ([1,2,3]) eligible for garbage collection.
"""

a = 3
a = 10
a = "hello"
a = [1,2,3]

a = [4,5,6]