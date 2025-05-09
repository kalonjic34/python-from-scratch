print(type({"a":1}))

print(isinstance(1, int))
print(isinstance({"a": 1}, dict))
print(isinstance([],list))
print(isinstance([], int))

print(isinstance(1,object))
print(isinstance(3.4,object))
print(isinstance(str,object))
print(isinstance(max,object))

print(isinstance([], (list,dict,int)))

class Person():
    pass

class Superhero(Person):
    pass

arnold = Person()
chris = Superhero()

print(isinstance(chris, Superhero))
print(isinstance(chris, Person))
print(isinstance(arnold, Person))
print(isinstance(arnold, Superhero))

print(issubclass(Superhero,Person))
print(issubclass(Person,Superhero))