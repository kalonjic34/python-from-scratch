animals = ["elephant","horse","cat","giraffe","cheetah","dog"]
long_length_of_animals = [animal for animal in animals if len(animal) > 5]
print(long_length_of_animals)

def is_long_animals(animal):
    return len(animal) > 5

print(list(filter(is_long_animals,animals)))
            