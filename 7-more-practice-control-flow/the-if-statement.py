"""
This script demonstrates the use of if statements in Python.

- The first if statement checks if 5 is greater than 3, which is true, so it prints two lines.
- The second if statement checks if 6 is greater than 20, which is false, so nothing is printed.
- The third if statement checks if the string "chris" is equal to "chris", which is true, so it prints a message.
- The fourth if statement checks if "dave" is equal to "Dave", which is false, so nothing is printed.
- The fifth if statement checks if "dave" is not equal to "Dave", which is true, so it prints two lines.
- The sixth if statement is always true, so it always prints.
- The seventh if statement is always false, so it never prints.
"""


if 5 > 3:
    print("Yep, thats true. This will be printed")
    print("Heres another line!")
    
if(6 > 20):
    print("Nope, that is false. That will not be printed")

if("chris" == "chris"):
    print("Great name!")
    
if "dave" == "Dave":
    print("Awesome name")
    
if "dave" != "Dave":
    print("haha, got you to print")
    print("Great success")
    
if True:
    print("Always true, always prints")
    
if False:
    print("Never true, not fit to print")