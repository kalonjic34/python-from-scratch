# Coding Exercise - Instance Methods

# Declare a Musician class that accepts age and income parameters.

# During the initialization of an object, assign these parameters to attributes with the same names.

# Declare an enter_club instance method:
# - If the musician is under 21 years old, the method should return "Access denied."
# - If the musician is 21 or older, the method should return "Access granted."

# Declare a play_show instance method:
# - This method should increment the musician's income by 5.

class Musician():
    def __init__(self,age,income):
        self.age = age
        self.income = income
        
    def enter_club(self):
        if self.age < 21:
            return "Access Denied!"
        elif self.age >= 21:
            return "Access Granted!"
        
    def play_show(self):
        self.income += 5
        
cliff = Musician(age=27,income=0)
print(cliff.age)
print(cliff.enter_club())
print(cliff.income)
cliff.play_show()
print(cliff.income)
cliff.play_show()
print(cliff.income)