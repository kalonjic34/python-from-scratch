def p(text):
    print(text)

p("Hello")
p("Goodbye")
p("Ok")

# p()
# TypeError: p() missing 1 required positional argument: 'text'

def add(a,b):
    print(f"The sum of {a} and {b} is {a+b}")
    
add(3,5)
add(-4,7)

# add()
# TypeError: add() missing 2 required positional arguments: 'a' and 'b'

# add(1)
# TypeError: add() missing 1 required positional argument: 'b'

# add(3,4,7)
# TypeError: add() takes 2 positional arguments but 3 were given
