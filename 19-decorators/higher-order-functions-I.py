def one():
    return 1

print(type(one))

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def calculate(func, a, b):
    return func(a, b)

print(calculate(add, 10,24))
print(calculate(subtract,8,14))
    