#  Coding Exercise - Equality and String Representation


# Declare a BusTrip class that accepts destination, bus_company, and price parameters.
# - During initialization, assign these parameters to attributes of the same names.

# Define a string representation for the class:
# - The string representation must follow this format:
#   "You paid 24.99 to Greyhound to go to Boston."
# - Replace the example values with the respective attributes for the object.

# Implement equality logic for BusTrip objects:
# - Two BusTrip objects are considered equal if:
#   - They have the same destination.
#   - They have the same bus_company.
#   - Their price is within 3 dollars of each other.

class BusTrip():
    def __init__(self,destination, company,price):
        self._destination = destination
        self._company = company
        self._price = price
        
    def __str__(self):
        return f"You paid ${self._price} to go {self._company} to go to {self._destination}"
        
    def __eq__(self, other_trip):
        destination = self._destination == other_trip._destination
        price = abs(self._price - other_trip._price) <= 3
        return destination and price
    
boston1 = BusTrip(destination = "Boston", company = "Greyhound", price = 24.99)
boston2 = BusTrip(destination = "Boston", company = "Megabus", price = 22.99)
boston3 = BusTrip(destination = "Boston", company = "Megabus", price = 49.99)
philly = BusTrip(destination = "Philadelphia", company = "Peter Pan", price = 12.99)

print(boston1)  # Paid 24.99 to Greyhound to go to Boston.
print(boston1 == philly)  # False - different destinations
print(boston1 == boston2)  # True - same destination and insignificant price difference
print(boston1 == boston3)  # False - large price difference