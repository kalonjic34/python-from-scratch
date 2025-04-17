# README: Classes: Inheritance

This document summarizes the key concepts and lessons learned while exploring inheritance in Python. Inheritance allows classes to inherit attributes and methods from other classes, promoting code reuse and organization.

---

## 1. Define a Subclass
**File:** [define-a-subclass.py](define-a-subclass.py)

I created a `Store` class and a `CoffeeShop` subclass that inherits from it.

```python
class Store():
    def __init__(self):
        self.owner = "Chris"
        
    def exclaim(self):
        return "Lots of stuff to buy, come inside!"

class CoffeeShop(Store):
    pass

starbucks = CoffeeShop()
print(starbucks.owner)  # Output: Chris
print(starbucks.exclaim())  # Output: Lots of stuff to buy, come inside!
```

**Key Insights:**
- The `CoffeeShop` subclass inherits attributes and methods from the `Store` class.

---

## 2. Subclassing with Additional Methods
**File:** [override-an-inherited-method-on-a-subclass.py](override-an-inherited-method-on-a-subclass.py)

I defined a `Teacher` class and a `CollegeProfessor` subclass that overrides a method.

```python
class Teacher():
    def teach_class(self):
        print("Teaching stuff...")
        
    def grab_lunch(self):
        print("Yum delicious")
        
    def grade_tests(self):
        print("F! F! F!")

class CollegeProfessor(Teacher):
    def grade_tests(self):
        print("A! A! A!")

teacher = Teacher()
professor = CollegeProfessor()

teacher.grade_tests()  # Output: F! F! F!
professor.grade_tests()  # Output: A! A! A!
```

**Key Insights:**
- Subclasses can override methods from their parent class to provide specific behavior.

---

## 3. Inheritance with Multiple Levels
**File:** [new-methods-on-subclasses.py](new-methods-on-subclasses.py)

I created an `Employee` class and extended it with `Manager` and `Director` subclasses.

```python
class Employee():
    def do_work(self):
        print("I'm working")
        
class Manager(Employee):
    def waste_time(self):
        print("Wow, this YouTube video is fun!")

class Director(Manager):
    def fire_employee(self):
        print("You are fired!")

d = Director()
d.do_work()  # Output: I'm working
d.waste_time()  # Output: Wow, this YouTube video is fun!
d.fire_employee()  # Output: You are fired!
```

**Key Insights:**
- Inheritance can create multiple levels, allowing for more specific subclasses.

---

## 4. Polymorphism with Inheritance
**File:** [polymorphism-I.py](polymorphism-I.py)

I demonstrated polymorphism by overriding the `__len__` method in a `Person` class.

```python
class Person():
    def __init__(self, name, height):
        self.name = name
        self.height = height
        
    def __len__(self):
        return self.height

values = [
    "Chris",
    [1, 2, 3],
    Person(name="Chris", height=71)
]

for value in values:
    print(len(value))  # Output: 5, 3, 71
```

**Key Insights:**
- Classes can define special methods like `__len__` to interact with built-in functions.

---

## 5. Polymorphism with Methods
**File:** [polymorphism-II.py](polymorphism-II.py)

I created a `Player` class and its subclasses, `HumanPlayer` and `ComputerPlayer`, demonstrating polymorphism.

```python
class Player():
    def __init__(self, games_played, victories):
        self.games_played = games_played
        self.victories = victories
        
    @property
    def win_ratio(self):
        return self.victories / self.games_played

class HumanPlayer(Player):
    def make_move(self):
        print("Let player make the decision!")

class ComputerPlayer(Player):
    def make_move(self):
        print("Run advanced algorithm to calculate best move!")

hp = HumanPlayer(games_played=30, victories=15)
cp = ComputerPlayer(games_played=1000, victories=999)

print(hp.win_ratio)  # Output: 0.5
print(cp.win_ratio)  # Output: 0.999
```

**Key Insights:**
- Subclasses can implement their own methods while sharing common properties from the parent class.

---

## 6. Multiple Inheritance
**File:** [multiple-inheritance-I.py](multiple-inheritance-I.py)

I created classes demonstrating multiple inheritance with `FrozenFood` and `Dessert`.

```python
class FrozenFood():
    def thaw(self, minutes):
        print(f"Thawing for {minutes} minutes")
        
    def store(self):
        print("Putting in the freezer!")

class Dessert():
    def add_weight(self):
        print("Putting on the pounds")
        
    def store(self):
        print("Putting in the refrigerator!")

class IceCream(FrozenFood, Dessert):
    pass

ic = IceCream()
ic.add_weight()
ic.thaw(5)
ic.store()  # Output: Putting in the freezer!
```

**Key Insights:**
- Classes can inherit from multiple parent classes, combining their behaviors.

---

## 7. Multiple Inheritance with Method Resolution Order
**File:** [multiple-inheritance-II.py](multiple-inheritance-II.py)

I demonstrated multiple inheritance with a `Restaurant` class and a `Bar` class.

```python
class Restaurant():
    def make_reservation(self, party_size):
        print(f"Booked a table for {party_size}")
        
class Steakhouse(Restaurant):
    pass

class Bar():
    def make_reservation(self, party_size):
        print(f"Book a lounge for {party_size}")
        
class BarAndGrill(Steakhouse, Bar):
    pass

bag = BarAndGrill()
bag.make_reservation(2)  # Output: Book a lounge for 2
print(BarAndGrill.mro())  # Outputs the method resolution order
```

**Key Insights:**
- The method resolution order (MRO) determines the order in which classes are searched for a method.

---

## 8. Multiple Inheritance with Class Hierarchy
**File:** [multiple-inheritance-III.py](multiple-inheritance-III.py)

I demonstrated multiple inheritance with a `FilmMaker` class and its subclasses.

```python
class FilmMaker():
    def give_interview(self):
        print("I love making movies")
        
class Director(FilmMaker):
    pass

class ScreenWriter(FilmMaker):
    def give_interview(self):
        print("I love writing scripts!")

class JackOfAllTrades(ScreenWriter, Director):
    pass

stallone = JackOfAllTrades()
stallone.give_interview()  # Output: I love writing scripts!
print(JackOfAllTrades.mro())  # Outputs the method resolution order
```

**Key Insights:**
- The order of inheritance affects method resolution and behavior in the class hierarchy.

---

## 9. Special Method Behavior
**File:** [name-mangling-for-privacy.py](name-mangling-for-privacy.py)

I demonstrated name mangling for privacy in a class.

```python
class Nonsense():
    def __init__(self):
        self.__some_attribute = "hello"
        
    def __some_method(self):
        print("This is coming from some_method")

class SpecialNonsense(Nonsense):
    pass

n = Nonsense()
sn = SpecialNonsense()

print(n._Nonsense__some_attribute)  # Accessing mangled attribute
print(sn._Nonsense__some_attribute)  # Accessing from subclass
print(n._Nonsense__some_method())    # Accessing mangled method
print(sn._Nonsense__some_method())    # Accessing from subclass
```

**Key Insights:**
- Name mangling provides a way to prevent attribute name collisions in subclasses.

---

## Practice Problems
**File:** [assignment.py](assignment.py)

### 1. HardwareStore Subclass
I created a `HardwareStore` subclass that inherits from the `Store` superclass.

```python
class Store():
    def __init__(self):
        self.owner = "Boris"
    
    def exclaim(self):
        return "I'm defined in the superclass!"

class HardwareStore(Store):
    pass

home_depot = HardwareStore()
print(home_depot.owner)  # Output: Boris
print(home_depot.exclaim())  # Output: I'm defined in the superclass!
```

### 2. Clothing and Socks
I defined a `Clothing` superclass and a `Socks` subclass that overrides methods.

```python
class Clothing():
    def wear(self):
        return "I'm wearing this fashionable piece of clothing!"
    
    def sell(self):
        return "Buy my piece of clothing!"

class Socks(Clothing):
    def lose_one(self):
        return "Where did my other one go?"
    
    def wear(self):
        return "Take a look at my socks! They're gorgeous!"
    
    def sell(self):
        return "Buy my socks!"

clean_socks = Socks()
print(clean_socks.wear())  # Output: Take a look at my socks! They're gorgeous!
print(clean_socks.lose_one())  # Output: Where did my other one go?
```

### 3. Musician and Drummer
I created a `Musician` class and a `Drummer` subclass that uses `super()`.

```python
class Musician():
    def __init__(self, name):
        self.name = name
        self.albums = []
    
    def release_album(self, title):
        self.albums.append(title)

class Drummer(Musician):
    def __init__(self, name, stamina):
        super().__init__(name)
        self.stamina = stamina

lars = Drummer(name="Lars", stamina=2)
lars.release_album("Ride the Lightning")
print(lars.albums)  # Output: ['Ride the Lightning']
```

### 4. Dental Health Routine
I created a dental health routine with various items.

```python
import random

class DentalHealthItem():
    def __init__(self, price):
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
floss = Floss(price=1.99)
mouthwash = Mouthwash(price=7.99)

dental_health_kit = [toothbrush, floss, mouthwash]
random.shuffle(dental_health_kit)

actions = [item.use() for item in dental_health_kit]
print(actions)  # Output: Randomly shuffled actions
```

---

## Summary

Through these exercises, I gained a comprehensive understanding of:
- The principles of inheritance in Python.
- Method overriding and the use of polymorphism.
- The organization of classes into hierarchies.
- The implementation of multiple inheritance and method resolution order.
- The concept of name mangling for privacy in class attributes.

These concepts are essential for writing clean, maintainable, and organized object-oriented Python code.