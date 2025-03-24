print('Today is a good day to learn Python')
print('Python is fun')
print("Python's string are easy to use")
print('We can include "quotes" in strings')
print("Hello "+"world")

greeting = 'Hello'
name = 'Chris'
# name = input('Please enter your name: ')
print(greeting + name)

# If i want space, i can add that too
print(greeting+' '+name)

age = 24 
print(age)

print(type(greeting))
print(type(age))

age_in_words = '2 years'
# TypeError: can only concatenate str (not "int") to str      
# Proving that python is a strongly typed
print(name +" is "+ age+ " years old")
print(type(age))