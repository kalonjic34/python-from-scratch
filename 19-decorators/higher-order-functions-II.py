def calculator(operation):
    def add(a,b):
        return a + b
    
    def subtract(a,b):
        return a - b
    
    if operation == "add":
        return add
    elif operation == "subtract":
        return subtract
    
print(calculator("add")(10,3))
print(calculator("subtract")(22,12))

def sqaure(num):
    return num ** 2

def cube(num):
    return num ** 3

def times10(num):
    return num * 10

operations = [sqaure,cube,times10]

for func in operations:
    print(func(5))