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

#  Coding Exercise - Protected Attributes

# Let's say we want to model a Book as a Python object.

# - A Book has an author and a publisher, which are characteristics that cannot change.
# - A Book also has a page_count, which could be altered if you rip some pages out.

# Declare a Book class that accepts author, publisher, and page_count parameters.
# - Each of the parameters should be assigned to an attribute.
# - The author and publisher attributes should be designated as protected (use an underscore).
# - The page_count attribute should be designated as public.

class Book():
    def __init__(self,author,publisher,page_count):
        self._author = author
        self._publisher = publisher
        self.page_count = page_count

# Define a copyright instance method that returns a string with information about the copyright.
# - It should use the string below, where "Grant Cardone" is the value of the protected author attribute
# and "10X Enterprises" is the value of the protected publisher attribute.
# Copyright Grant Cardone, 10X Enterprises

    def copyright(self):
        return f"=> Copyright {self._author}, {self._publisher}"

# The public page_count attribute can always be manually modified.
# - However, we can still define an instance method that modifies it.

# Declare a rip_in_half instance method.
# - If the Book has more than 1 page, it should halve the page_count.
# - If the Book has 1 page or less, it should set the page_count to 0.

    def rip_in_half(self):
        if self.page_count > 1:
            self.page_count /= 2
        else:
            self.page_count = 0
 
    
book = Book(author="Grant Cardone",publisher="10X Enterprises",page_count=10)

print(book.page_count)
book.rip_in_half()
print(book.page_count)
book.rip_in_half()
print(book.page_count)
book.rip_in_half()
print(book.page_count)
book.rip_in_half()
print(book.page_count)
book.rip_in_half()
print(book.page_count)
book.rip_in_half()
print(book.page_count)

# Declare a PizzaPie class that accepts a total_slices parameter.
# - During the instantiation, assign the parameter to an attribute of the same name.

# A PizzaPie object should also be initialized with a _slices_eaten protected attribute set to 0.

class PizzaPie():
    def __init__(self,total_slices):
        self.total_slices = total_slices
        self._slice_eaten = 0

    @property
    def slices_eaten(self):
        return self._slice_eaten
    
    @slices_eaten.setter
    def slices_eaten(self, slice_eaten):
        if slice_eaten <= self.total_slices:
            self._slice_eaten = slice_eaten
    
    @property
    def percentage(self):
        return self._slice_eaten / self.total_slices
    
# Define a _slices_eaten property:
# - The getter method should retrieve the value of the _slices_eaten attribute.
# - The setter method should allow updating _slices_eaten, but only if the new value is less than total_slices.

# Define a percentage property:
# - This property should calculate the percentage of the pie that has been eaten
#   (slices eaten divided by total slices).
# - This percentage property should be read-only.

cheese = PizzaPie(8)  # Create a pizza with 8 slices
cheese.slices_eaten = 2
print(cheese.percentage)  # Outputs: 0.25

cheese.slices_eaten = 4
print(cheese.percentage)  # Outputs: 0.5

cheese.slices_eaten = 10  # slices_eaten should not change; there are only 8 slices
print(cheese.percentage)  # Outputs: 0.5

# ERROR: AttributeError
# cheese.percentage = 0.50  # Trying to directly set percentage causes an AttributeError.
    
# Coding Exercise - Class Methods

# Declare a Chocolate class that accepts a cacao_content attribute.

# Define a sweet class method:
# - This should return a Chocolate object with cacao_content set to 30.

# Define a semisweet class method:
# - This should return a Chocolate object with cacao_content set to 50.

# Define a bittersweet class method:
# - This should return a Chocolate object with cacao_content set to 70.

# Define a bitter class method:
# - This should return a Chocolate object with cacao_content set to 99.
            
class Chocolate():
    def __init__(self,cacao_content):
        self.cacao_content = cacao_content
        
    @classmethod
    def sweet(cls):
        return cls(cacao_content = 30)
    
    @classmethod
    def semisweet(cls):
        return cls(cacao_content = 50)
    
    @classmethod
    def bittersweet(cls):
        return cls(cacao_content = 70)
    
    @classmethod
    def bitter(cls):
        return cls(cacao_content = 99)
    