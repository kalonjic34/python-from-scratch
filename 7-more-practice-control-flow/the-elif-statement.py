"""
This script contains two functions: 
1. `positive_or_negative`: Determines if a number is positive, negative, or zero.
2. `calculator`: Performs basic arithmetic operations (add, subtract, multiply, divide) based on the given operation.
"""

def positive_or_negative(number):
    if number > 0:
        return "Positive!"
    elif number < 0:
        return "Negative!"
    else:
        return "Neither its zero"
    
print(positive_or_negative(5))
print(positive_or_negative(-3))
print(positive_or_negative(0))

def calculator(operation,a,b):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b
    print("I dont know what you want me to do")
    
print(calculator("add",3,4))
print(calculator("subtract",3,4))
print(calculator("multiply",3,4))
print(calculator("divide",3,4))
print(calculator("transmorify",3,4))
    