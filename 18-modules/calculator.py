creator = "Christian"
PI = 3.14159

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def area(radius):
    return PI * radius * radius

if __name__ == "__main__":
    print("This will only run when calculator is being executed as a script")
    print(subtract(3,5))