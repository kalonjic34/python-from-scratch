"""
This script demonstrates the use of the enumerate function in Python.
The enumerate function is used to iterate over a list while keeping track of the index.
"""

errands = ["Go to the gym","Grab lunch", "Get promoted at work","Sleep"]

print(enumerate(errands))
# <enumerate object at 0x000001808F3BDB20>

for index,task in  enumerate(errands, 1):
    print(f"{task} is number {index} on my list of things to do today!")
    