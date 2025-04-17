print(" - Coding Exercise SOLUTION Define a Subclass\n")

# Declare a HardwareStore subclass that inherits from the Store superclass.

# Do not define any attributes and methods on the subclass.

# Use the pass keyword to avoid a class body in HardwareStore.

# Instantiate a new instance of the HardwareStore class and assign it to a home_depot variable.

# Access the value of the "owner" attribute on your HardwareStore instance.

# Invoke the exclaim instance method on your HardwareStore instance.

class Store():
    def __init__(self):
        self.owner = "Boris"
    
    def exclaim(self):
        return "Im defined in the superclass!"
    
class HardwareStore(Store):
    pass

home_depot = HardwareStore()
print(home_depot.owner)
print(home_depot.exclaim())

print("\n - Coding Exercise SOLUTION Override a Method on Subclass\n")

# Define a Clothing superclass with two instance methods:
# - wear(), which should return "I'm wearing this fashionable piece of clothing!"
# - sell(), which should return "Buy my piece of clothing!"

# Then, define a Socks subclass that:
# - Inherits from Clothing
# - Has a lose_one() method that returns "Where did my other one go?"
# - Overrides wear() to return "Take a look at my socks! They're gorgeous!"
# - Overrides sell() to return "Buy my socks!"

class Clothing():
    def wear(self):
        return "Im wearing this fashionable piece of clothing!"
    def sell(self):
        return "Buy mu piece of clothing"
    
class Socks():
    def lose_one(self):
        return "Where did my other one go?"
    def wear(self):
        return "Take a look at my socks! They are gorgeous!"
    def sell(self):
        return "Buy my socks!"
    
clean_socks = Socks()
print(clean_socks.wear())
print(clean_socks.lose_one())

print("\n - Coding Exercise SOLUTION The super Function\n")

# Declare a Musician class that accepts a name argument in its initialization.
# The initialization should assign a name argument to a name attribute.
# In addition, each Musician object should have an albums attribute that begins as an empty list.
# Define a release_album instance method on a Musician that accepts a title (string).
# It should append the string to the end of the list held by the albums attribute.

# Declare a Drummer subclass that inherits from the Musician superclass.
# In addition to a name, a drummer should also have a stamina attribute represented by an integer.
# The subclass should invoke the Musician superclass's initialization procedure and pass it the drummer's name.
# It should also set the stamina attribute in its own initialization process.


class Musician():
    def __init__(self,name):
        self.name = name
        self.albums = []
    
    def release_album(self,title):
        self.albums.append(title)
        
class Drummer(Musician):
    def __init__(self, name,stamina):
        super().__init__(name)
        self.stamina = stamina


lars = Drummer(name="Lars", stamina=2)
print(lars.name)    # Output: "Lars"
print(lars.stamina) # Output: 2
print(lars.albums)  # Output: []

lars.release_album("Ride the Lightning")
print(lars.albums)  # Output: ["Ride the Lightning"]

lars.release_album("Master of Puppets")
print(lars.albums)  # Output: ["Ride the Lightning", "Master of Puppets"]

print("\n - Coding Exercise SOLUTION Polymorphism\n")

# We're modeling a routine for proper dental health, which includes brushing our teeth,
# flossing, and using mouthwash. The order of these three varies from person to person.

# 1. Declare a DentalHealthItem class. Its initialization should set a "price" attribute.

# 2. Declare a Toothbrush subclass that inherits from DentalHealthItem.
#    On it, define a "use" instance method that returns "Brushing the teeth".

# 3. Declare a Floss subclass that inherits from DentalHealthItem.
#    On it, define a "use" instance method that returns "Flossing the teeth".

# 4. Declare a Mouthwash subclass that inherits from DentalHealthItem.
#    On it, define a "use" instance method that returns "Washing the teeth".

# 5. Instantiate an instance of a Toothbrush and assign it to a "toothbrush" variable.
# 6. Instantiate an instance of a Floss and assign it to a "floss" variable.
# 7. Instantiate an instance of a Mouthwash and assign it to a "mouthwash" variable.

# 8. Declare a "dental_health_kit" variable. It should be a list that stores the three objects.

# 9. Import the "random" module (see last lesson for reference).
# 10. Invoke the "shuffle" function from the module, passing in the dental_health_kit list.
#     This will mutate the list, randomizing the order of its elements.

# 11. Use list comprehension to invoke the "use" method on all three objects in "dental_health_kit".

# 12. Assign the resulting list of strings to an "actions" variable.

import random

class DentalHealthItem():
    def __init__(self,price):
        self.price = price
        
class Toothbrush(DentalHealthItem):
    def use(self):
        return "Brushing the teeth"

class Floss(DentalHealthItem):
    def use(self):
        return "Flossing the teeth"
    
class Mouthwash(DentalHealthItem):
    def use(self):
        return "Washing the teeth"
    
toothbrush = Toothbrush(price=4.99)
floss = Floss(price= 1.99)
mouthwash = Mouthwash(price=7.99)

dental_health_kit = [toothbrush, floss, mouthwash]
random.shuffle(dental_health_kit)

actions = [item.use() for item in dental_health_kit]
print(actions)