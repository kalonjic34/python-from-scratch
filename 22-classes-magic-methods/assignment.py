print(" - Coding Exercise - Equality and String Representation\n")
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

print("\n - Coding Exercise namedtuple\n")

#  Coding Exercise namedtuple

# Use the namedtuple function to create a GymExercise class.
# The class should have three attributes: name, weight, and reps.

# Assign a squat variable to a GymExercise tuple object with:
# - Name: "squat"
# - Weight: 265
# - Rep count: 3

# Assign a bench variable to a GymExercise tuple object with:
# - Name: "benchpress"
# - Weight: 185
# - Rep count: 5

# Assign a deadlift variable to a GymExercise tuple object with:
# - Name: "deadlift"
# - Weight: 225
# - Rep count: 6

# Assign a press variable to a GymExercise tuple object with:
# - Name: "press"
# - Weight: 120
# - Rep count: 8

import collections

GymExercise = collections.namedtuple("GymExercise",["name","weight","reps"])

squat = GymExercise(name="squat", weight=265, reps=3)
print(squat.name)
print(squat.weight)
print(squat.reps)

bench = GymExercise(name="benchpress", weight=185, reps=5)
print(bench.name)
print(bench.weight)
print(bench.reps)

deadlift = GymExercise("deadlift",225, 6)
print(deadlift.name)
print(deadlift.weight)
print(deadlift.reps)

press = GymExercise("press",120, 8)
print(press.name)
print(press.weight)
print(press.reps)
