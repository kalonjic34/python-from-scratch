employee = ("Bob", "Johnson", "Manager", 50)

# first_name = employee[0]
# last_name = employee[1]
# position = employee[2]
# age = employee[3]

first_name, last_name, position, age = employee
print(first_name,last_name,position,age)

subject,verb,adjective = ["Python","is", "fun"]
print(subject)
print(verb)
print(adjective)

# first_name, last_name, title = employee
# ValueError: too many values to unpack (expected 3)

# first_name, last_name, position, age, salary = employee 
# ValueError: not enough values to unpack (expected 5, got 4)

a = 5
b = 10

b, a = a, b
print(a)
print(b)

