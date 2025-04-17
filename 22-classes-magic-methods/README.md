# README: Magic Methods in Python

This document summarizes the key concepts and lessons learned while exploring magic methods in Python. Magic methods, also known as dunder (double underscore) methods, allow for the customization of object behavior in various operations.

---

## 1. Truthiness with `__bool__`
**File:** [truthiness-with-the-__bool__-method.py](truthiness-with-the-__bool__-method.py)

The `__bool__` method defines the truth value of an object.

```python
class Emotion():
    def __init__(self, positivity, negativity):
        self.positivity = positivity
        self.negativity = negativity
        
    def __bool__(self):
        return self.positivity > self.negativity

my_emotional_state = Emotion(50, 75)
if my_emotional_state:
    print("This will not print.")

my_emotional_state.positivity = 100
if my_emotional_state:
    print("This WILL print.")
```

**Key Insights:**
- The `__bool__` method allows custom truthiness evaluation for objects.

---

## 2. Destructor with `__del__`
**File:** [the-__del__-method.py](the-__del__-method.py)

The `__del__` method defines behavior when an object is about to be destroyed.

```python
class Garbage():
    def __del__(self):
        print("This is my last breath!")

g = Garbage()
g = [1, 2, 3]
```

**Key Insights:**
- The `__del__` method can be used for cleanup actions before an object is deleted.

---

## 3. String Representation with `__str__` and `__repr__`
**File:** [string-representation-with-the-__str__-and-__repr__-methods.py](string-representation-with-the-__str__-and-__repr__-methods.py)

The `__str__` method defines a user-friendly string representation, while `__repr__` provides an unambiguous representation.

```python
class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"
        
    def __repr__(self):
        return f'Card("{self.rank}", "{self.suit}")'

c = Card("Ace", "Spade")
print(c)  # Calls __str__
print(repr(c))  # Calls __repr__
```

**Key Insights:**
- Use `__str__` for a readable representation and `__repr__` for an official representation.

---

## 4. Namedtuples and Attributes
**File:** [namedtuple.py](namedtuple.py)

Namedtuples provide a lightweight way to create classes with simple attributes.

```python
import collections

Book = collections.namedtuple("Book", ["title", "author"])
animal_farm = Book("Animal Farm", "George Orwell")
print(animal_farm.title)  # Output: Animal Farm
```

**Key Insights:**
- Namedtuples are great for creating simple classes with named fields.

---

## 5. Comparison Operations with Magic Methods
**File:** [magic-methods-for-comparison-operations.py](magic-methods-for-comparison-operations.py)

Magic methods allow customization of comparison operations.

```python
class Student():
    def __init__(self, math, history, writing):
        self.math = math
        self.history = history
        self.writing = writing
        
    @property
    def grades(self):
        return self.math + self.history + self.writing
    
    def __eq__(self, other_student):
        return self.grades == other_student.grades
        
bob = Student(90, 90, 90)
matt = Student(100, 90, 80)
print(bob == matt)  # Output: False
```

**Key Insights:**
- Implement `__eq__`, `__gt__`, and other comparison methods to customize object comparisons.

---

## 6. Length with `__len__`
**File:** [length-with-the-__len__-method.py](length-with-the-__len__-method.py)

The `__len__` method defines the behavior of the built-in `len()` function.

```python
class Library():
    def __init__(self, *books):
        self.books = books
        
    def __len__(self):
        return len(self.books)

l1 = Library("Book1", "Book2")
print(len(l1))  # Output: 2
```

**Key Insights:**
- Implementing `__len__` allows the use of the `len()` function on custom objects.

---

## 7. Indexing with `__getitem__` and `__setitem__`
**File:** [indexing-with-the-__getitem__-and-__setitem__.py](indexing-with-the-__getitem__-and-__setitem__.py)

Custom indexing behavior can be defined using `__getitem__` and `__setitem__`.

```python
class CrayonBox():
    def __init__(self):
        self.crayons = []
        
    def add(self, crayon):
        self.crayons.append(crayon)
        
    def __getitem__(self, index):
        return self.crayons[index]
    
    def __setitem__(self, index, value):
        self.crayons[index] = value

cb = CrayonBox()
cb.add("Blue")
print(cb[0])  # Output: Blue
```

**Key Insights:**
- Custom indexing allows objects to behave like sequences.

---

## 8. Equality with `__eq__`
**File:** [equality-with-the-__eq__-method.py](equality-with-the-__eq__-method.py)

The `__eq__` method defines the behavior of the equality operator `==`.

```python
class Student():
    def __init__(self, math, history, writing):
        self.math = math
        self.history = history
        self.writing = writing
        
    @property
    def grades(self):
        return self.math + self.history + self.writing
    
    def __eq__(self, other_student):
        return self.grades == other_student.grades

bob = Student(90, 90, 90)
joe = Student(40, 45, 50)
print(bob == joe)  # Output: False
```

**Key Insights:**
- Implementing `__eq__` allows for custom equality checks based on object attributes.

---

## 9. Documentation with `__doc__`
**File:** [docstrings.py](docstrings.py)

The `__doc__` attribute stores the documentation string of a module, class, or function.

```python
import sushi

print(sushi.__doc__)
print(sushi.fish.__doc__)
```

**Key Insights:**
- Use `__doc__` for accessible documentation of code elements.

---

## Practice Problems
**File:** [assignment.py](assignment.py)

### BusTrip Class
I created a `BusTrip` class that accepts destination, bus company, and price parameters. The class includes a string representation and equality logic.

```python
class BusTrip():
    def __init__(self, destination, company, price):
        self._destination = destination
        self._company = company
        self._price = price
        
    def __str__(self):
        return f"You paid ${self._price} to go {self._company} to go to {self._destination}"
        
    def __eq__(self, other_trip):
        destination = self._destination == other_trip._destination
        price = abs(self._price - other_trip._price) <= 3
        return destination and price

boston1 = BusTrip(destination="Boston", company="Greyhound", price=24.99)
boston2 = BusTrip(destination="Boston", company="Megabus", price=22.99)
boston3 = BusTrip(destination="Boston", company="Megabus", price=49.99)

print(boston1)  # Output: You paid $24.99 to go Greyhound to go to Boston.
print(boston1 == boston2)  # Output: True
print(boston1 == boston3)  # Output: False
```

### GymExercise Namedtuple
I used the `namedtuple` function to create a `GymExercise` class with attributes: name, weight, and reps.

```python
import collections

GymExercise = collections.namedtuple("GymExercise", ["name", "weight", "reps"])

squat = GymExercise(name="squat", weight=265, reps=3)
print(squat.name)  # Output: squat
print(squat.weight)  # Output: 265
```

### Custom Indexing and Iteration
I defined a `Car` class and a `Dealership` class to manage a collection of cars.

```python
class Car():
    def __init__(self, maker, model, year):
        self.maker = maker
        self.model = model
        self.year = year
        
class Dealership():
    def __init__(self):
        self.cars = []
        
    def accept_delivery(self, car):
        self.cars.append(car)
        
    def __getitem__(self, index):
        return self.cars[index]
        
    def __setitem__(self, index, value):
        self.cars[index] = value

f150 = Car(maker="Ford", model="F-150", year=2019)
dealership = Dealership()
dealership.accept_delivery(f150)

print(dealership[0].year)  # Output: 2019
```

---

## Summary

Through these exercises, I gained a comprehensive understanding of:
- Creating and using classes and objects.
- Implementing magic methods for custom behavior.
- Using namedtuples for simple data structures.
- Custom indexing and iteration in classes.
- Defining equality and string representation methods.

These concepts are essential for writing clean, maintainable, and object-oriented Python code.