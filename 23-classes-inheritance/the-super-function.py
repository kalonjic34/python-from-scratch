class Animal():
    def __init__(self,name):
        self.first_name = name
        
    def eat(self, food):
        return f"{self.name} is enjoying the {food}"
    
class Dog(Animal):
    def __init__(self, name,breed):
        super().__init__(name)
        self.breed = breed

watson = Dog("Watson", "Golden Retriever")
print(watson.first_name)
print(watson.breed)

