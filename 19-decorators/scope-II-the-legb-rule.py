# x = 15

def outer():   
    # Enclosing function scope
    # x = 10 
    def inner():
        # local scope
        # x = 5
        return len
    
    return inner()

print(outer()("Python"))