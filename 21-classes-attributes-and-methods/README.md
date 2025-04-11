# Classes: Attributes and Methods

This document provides a detailed summary of the key concepts and lessons I learned while exploring attributes and methods in Python classes. Attributes store data about an object, while methods define the behavior of an object. Below is a breakdown of the topics covered and the insights gained.

---

## 1. Instance Attributes and Methods
File: [instance-methods.py](21-classes-attributes-and-methods/instance-methods.py)

Instance attributes store data unique to each object, while instance methods define behavior specific to an object.

```python
class Pokemon():
    def __init__(self, name, specialty, health=100):
        self.name = name
        self.specialty = specialty
        self.health = health

    def roar(self):
        print("Raaarrr!")

    def describe(self):
        print(f"I am {self.name}. I am a {self.specialty} Pokemon!")

    def take_damage(self, amount):
        self.health -= amount

squirtle = Pokemon("Squirtle", "Water")
squirtle.describe()  # Output: I am Squirtle. I am a Water Pokemon!
squirtle.take_damage(20)
print(squirtle.health)  # Output: 80
```

**Key Insights:**
- Instance attributes are defined in the `__init__` method and are unique to each object.
- Instance methods operate on the object's attributes and define its behavior.

---

## 2. Protected Attributes and Methods
File: [protected-attributes-and-methods.py](21-classes-attributes-and-methods/protected-attributes-and-methods.py)

Protected attributes and methods are indicated by a single underscore (`_`) and are intended for internal use within the class.

```python
class SmartPhone():
    def __init__(self):
        self._company = "Apple"
        self._firmware = 10.0

    def update_firmware(self):
        self._firmware += 1

iphone = SmartPhone()
print(iphone._company)  # Output: Apple
iphone.update_firmware()
print(iphone._firmware)  # Output: 11.0
```

**Key Insights:**
- Protected attributes and methods are not enforced by Python but are a convention to indicate internal use.

---

## 3. Properties with `property` Method
File: [define-properties-with-property-method.py](21-classes-attributes-and-methods/define-properties-with-property-method.py)

The `property` method allows you to define getter and setter methods for attributes.

```python
class Height():
    def __init__(self, feet):
        self._inches = feet * 12

    def _get_feet(self):
        return self._inches / 12

    def _set_feet(self, feet):
        if feet >= 0:
            self._inches = feet * 12

    feet = property(_get_feet, _set_feet)

h = Height(5)
print(h.feet)  # Output: 5.0
h.feet = 6
print(h.feet)  # Output: 6.0
```

**Key Insights:**
- Properties provide a clean way to control access to attributes while maintaining encapsulation.

---

## 4. Properties with Decorators
File: [define-properties-with-decorators.py](21-classes-attributes-and-methods/define-properties-with-decorators.py)

The `@property` decorator simplifies the creation of getter and setter methods.

```python
class Currency():
    def __init__(self, dollars):
        self._cents = dollars * 100

    @property
    def dollars(self):
        return self._cents / 100

    @dollars.setter
    def dollars(self, dollars):
        if dollars >= 0:
            self._cents = dollars * 100

bank_account = Currency(500)
print(bank_account.dollars)  # Output: 500.0
bank_account.dollars = 1000
print(bank_account.dollars)  # Output: 1000.0
```

**Key Insights:**
- The `@property` decorator provides a more Pythonic way to define properties.

---

## 5. Class Attributes
File: [class-attributes.py](21-classes-attributes-and-methods/class-attributes.py)

Class attributes are shared across all instances of a class.

```python
class Counter():
    count = 0

    def __init__(self):
        Counter.count += 1

c1 = Counter()
c2 = Counter()
print(Counter.count)  # Output: 2
```

**Key Insights:**
- Class attributes are defined outside the `__init__` method and are shared by all instances.

---

## 6. Class Methods
File: [class-methods.py](21-classes-attributes-and-methods/class-methods.py)

Class methods operate on the class itself rather than individual instances.

```python
class SushiPlatter():
    @classmethod
    def lunch_special(cls):
        return cls(salmon=2, tuna=2, shrimp=2, squid=0)

lunch = SushiPlatter.lunch_special()
print(lunch.salmon)  # Output: 2
```

**Key Insights:**
- Class methods are defined using the `@classmethod` decorator and take `cls` as their first parameter.

---

## 7. Static Methods
File: [static-methods.py](21-classes-attributes-and-methods/static-methods.py)

Static methods do not operate on the class or its instances and are used for utility functions.

```python
class WeatherForecast():
    @staticmethod
    def convert_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5 / 9

print(WeatherForecast.convert_to_celsius(100))  # Output: 37.77777777777778
```

**Key Insights:**
- Static methods are defined using the `@staticmethod` decorator and do not require `self` or `cls`.

---

## 8. Attribute Lookup Order
File: [attribute-lookup-order.py](21-classes-attributes-and-methods/attribute-lookup-order.py)

Python checks for attributes in the following order: instance attributes, class attributes, and parent class attributes.

```python
class Example():
    data = "Class attribute"

e1 = Example()
e1.data = "Instance attribute"
print(e1.data)  # Output: Instance attribute
del e1.data
print(e1.data)  # Output: Class attribute
```

**Key Insights:**
- Instance attributes take precedence over class attributes during lookup.

---

## 9. Practice Problems
File: [assignment.py](21-classes-attributes-and-methods/assignment.py)

This section focuses on solving practical problems using attributes and methods. Below are some examples:

### 9.1. Instance Methods
This exercise demonstrates how to define and use instance methods to encapsulate behavior specific to an object.

```python
class Musician():
    def __init__(self, age, income):
        self.age = age
        self.income = income

    def enter_club(self):
        return "Access granted." if self.age >= 21 else "Access denied."

    def play_show(self):
        self.income += 5

cliff = Musician(age=27, income=0)
print(cliff.enter_club())  # Output: Access granted.
cliff.play_show()
print(cliff.income)  # Output: 5
```
**Key Insights:**
- Instance methods operate on the attributes of a specific object.
- They allow objects to encapsulate behavior and interact with their own data.

---

### 9.2. Protected Attributes
This exercise demonstrates how to use protected attributes to indicate that certain attributes are intended for internal use.

```python
class Book():
    def __init__(self, author, publisher, page_count):
        self._author = author
        self._publisher = publisher
        self.page_count = page_count

book = Book("Author Name", "Publisher Name", 300)
print(book.page_count)  # Output: 300
```

**Key Insights:**
- Protected attributes (indicated by a single underscore) are a convention to signal that they should not be accessed directly outside the class.
- They help maintain encapsulation and prevent unintended modifications.

---

## Summary

Through these exercises, I gained a comprehensive understanding of:
- Instance, class, and static methods.
- Using properties to control access to attributes.
- The difference between instance and class attributes.
- Attribute lookup order and the use of protected attributes.

These concepts are essential for writing clean, maintainable, and object-oriented Python code.