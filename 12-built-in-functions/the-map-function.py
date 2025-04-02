numbers = [4,8,15,16,23,42]

cubes = [number ** 3 for number in numbers]
print(cubes)

def cube(number):
    return number ** 3

print(list(map(cube, numbers)))

animals = ["Cat", "Bear", "Zebra", "Cheetah"]
print([len(animal) for animal in animals])

print(list(map(len,animals)))

def list_of_animals(animal):
    return len(animal)

print(list(map(list_of_animals, animals)))