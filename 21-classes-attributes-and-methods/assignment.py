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