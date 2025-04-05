# Define an invoke_thrice function.
# It should accept a single argument (which will be a function).
# In its body, the invoke_thrice function should invoke
# the function that's passed in exactly three times.

def invoke_thrice(func):
    func()
    func()
    func()
    
def sample():
    print("A")
    print("B")
    print("C")
    
def another_sample():    
    print("D")
    print("E")
        

print(invoke_thrice(sample))
print()
print(invoke_thrice(another_sample))

# Define an "outer" function that accepts no arguments.
# Inside the body of "outer", define an "inner" function.
# The "inner" function should return the value 5.
# From "outer", return the uninvoked "inner" function.

def outer():
    def inner():
        return 5
    
    return inner

print(outer()())

# Define a global "a" variable assigned to the value 1.

# Declare a "modify_a" function that accepts a single argument.
# It should overwrite the value of the global variable "a" with the argument.

a = 1

def modify_a(value):
    global a
    a = value

print(a)
modify_a(10)
print(a)