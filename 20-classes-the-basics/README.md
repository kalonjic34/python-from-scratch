# Classes: The Basics

This document provides a detailed summary of the key concepts and lessons I learned while exploring classes in Python. Classes are the foundation of object-oriented programming, allowing us to create reusable blueprints for objects. Below is a breakdown of the topics covered and the insights gained.

---

## 1. Class Definition and Instantiation
File: [class-definition-and-instantiation.py](20-classes-the-basics/class-definition-and-instantiation.py)

Classes are defined using the `class` keyword. Objects are instantiated from classes to represent specific instances.

```python
class Person():
    pass

class DatabaseConnection():
    pass

chris = Person()
sam = Person()

print(chris)  # Output: <__main__.Person object at ...>
print(sam)    # Output: <__main__.Person object at ...>
```

**Key Insights:**
- Classes are blueprints for creating objects.
- Objects are instances of classes.

---

## 2. The `__init__` Method
File: [the__init__method.py](20-classes-the-basics/the__init__method.py)

The `__init__` method is a special method that initializes an object when it is created.

```python
class Guitar():
    def __init__(self):
        print(f"A new guitar is being created! This object is {self}")

acoustic = Guitar()
electric = Guitar()
```

**Key Insights:**
- The `__init__` method is automatically called when an object is instantiated.
- It is used to initialize the object's attributes.

---

## 3. Adding Attributes to Objects
File: [adding_attributes_to_objects.py](20-classes-the-basics/adding_attributes_to_objects.py)

Attributes can be added to objects dynamically after they are created.

```python
class Guitar():
    pass

acoustic = Guitar()
acoustic.wood = "Mahogany"
acoustic.strings = 6

print(acoustic.wood)  # Output: Mahogany
print(acoustic.strings)  # Output: 6
```

**Key Insights:**
- Attributes can be added to objects dynamically, but this is not recommended for consistency.
- Use the `__init__` method to define attributes during object creation.

---

## 4. Setting Object Attributes in the `__init__` Method
File: [setting_object_attributes_in_the__init__method.py](20-classes-the-basics/setting_object_attributes_in_the__init__method.py)

Attributes can be initialized in the `__init__` method to ensure all objects have consistent attributes.

```python
class Guitar():
    def __init__(self, wood):
        self.wood = wood

acoustic = Guitar("Alder")
electric = Guitar("Mahogany")

print(acoustic.wood)  # Output: Alder
print(electric.wood)  # Output: Mahogany
```

**Key Insights:**
- Use the `__init__` method to define attributes for all objects of a class.
- This ensures consistency and avoids missing attributes.

---

## 5. Default Values for Attributes
File: [default-values-for-attributes.py](20-classes-the-basics/default-values-for-attributes.py)

Attributes can have default values, which are used if no value is provided during instantiation.

```python
class Book():
    def __init__(self, title, author, price=14.99):
        self.title = title
        self.author = author
        self.price = price

gatsby = Book("The Great Gatsby", "F. Scott Fitzgerald")
print(gatsby.price)  # Output: 14.99
```

**Key Insights:**
- Default values simplify object creation by providing fallback values.
- They make attributes optional during instantiation.

---

## 6. Practice Problems
File: [assignment.py](20-classes-the-basics/assignment.py)

This section focuses on solving practical problems using classes. Below are some examples:

### 6.1. Define and Instantiate Classes
This exercise demonstrates how to define a class and create multiple instances of it.

```python
class Country():
    pass

america = Country()
canada = Country()
mexico = Country()
```

**Key Insights:**
- Classes are blueprints for creating objects.
- Each object (instance) is independent and can have its own attributes and behavior.


---

### 6.2. Use the `__init__` Method
This exercise demonstrates how to use the `__init__` method to initialize attributes for objects during instantiation.

```python
class Musical():
    def __init__(self, name):
        self.name = name

rent = Musical("Rent")
mormon = Musical("Book of Mormon")
chicago = Musical("Chicago")

print(rent.name)  # Output: Rent
print(mormon.name)  # Output: Book of Mormon
print(chicago.name)  # Output: Chicago
```

**Key Insights:**
- The `__init__` method is automatically called when an object is created.
- It allows you to set up initial values for the object's attributes.

---

### 6.3. Default Attribute Values
This exercise demonstrates how to use default values for attributes in the `__init__` method.

```python
class Zombie():
    def __init__(self, health=100, brains_eaten=5):
        self.health = health
        self.brains_eaten = brains_eaten

bob = Zombie(80, 5)
alice = Zombie(120, 3)
default_zombie = Zombie()

print(bob.health)  # Output: 80
print(alice.brains_eaten)  # Output: 3
print(default_zombie.health)  # Output: 100
print(default_zombie.brains_eaten)  # Output: 5
```

**Key Insights:**
- Default values make attributes optional during instantiation.
- If no value is provided, the default value is used.


---

## Summary

Through these exercises, I gained a comprehensive understanding of:
- Defining and instantiating classes.
- Using the `__init__` method to initialize attributes.
- Adding attributes dynamically and using default values.

Classes are a powerful tool for organizing and structuring code in Python, enabling object-oriented programming.