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

