# Sets

This document provides a detailed summary of the key concepts and lessons I learned while exploring sets in Python. Sets are unordered collections of unique elements, making them useful for tasks like removing duplicates and performing mathematical set operations. Below is a breakdown of the topics covered and the insights gained.

---

## 1. Introduction to Sets
File: [intro-to-sets.py](17-sets/intro-to-sets.py)

Sets are unordered collections of unique elements. They do not allow duplicates and are not subscriptable.

```python
stocks = {"MSFT", "FB", "IBM", "FB"}
print(stocks)  # Output: {'MSFT', 'FB', 'IBM'}

prices = {1, 2, 3, 4, 5, 3, 4, 2}
print(prices)  # Output: {1, 2, 3, 4, 5}
```

---

## 2. The `set` Function
File: [the-set-function.py](17-sets/the-set-function.py)

The `set` function can be used to create a set from an iterable, automatically removing duplicates.

```python
philosophers = ["Plato", "Socrates", "Aristotle", "Socrates"]
philosophers_set = set(philosophers)
print(philosophers_set)  # Output: {'Plato', 'Socrates', 'Aristotle'}
```

---

## 3. The `add` and `update` Methods
File: [the-add-and-update-methods.py](17-sets/the-add-and-update-methods.py)

The `add` method adds a single element to a set, while the `update` method adds multiple elements.

```python
disney_characters = {"Mickey Mouse", "Elsa"}
disney_characters.add("Ariel")
disney_characters.update(["Donald Duck", "Goofy"])
print(disney_characters)
```

---

## 4. The `remove` and `discard` Methods
File: [the-remove-and-discard-methods.py](17-sets/the-remove-and-discard-methods.py)

The `remove` method removes an element from a set but raises a `KeyError` if the element is not found. The `discard` method removes an element without raising an error if the element is not found.

```python
agents = {"Mulder", "Scully", "Doggett"}
agents.remove("Doggett")
agents.discard("Skinner")  # No error if "Skinner" is not in the set
print(agents)
```

---

## 5. The `union` Method
File: [the-union-method.py](17-sets/the-union-method.py)

The `union` method combines two sets, returning a new set with all unique elements from both sets.

```python
candy_bars = {"Milky Way", "Snickers"}
sweet_things = {"Sour Patch Kids", "Snickers"}
print(candy_bars.union(sweet_things))  # Output: {'Milky Way', 'Snickers', 'Sour Patch Kids'}
```

---

## 6. The `intersection` Method
File: [the-intersection-method.py](17-sets/the-intersection-method.py)

The `intersection` method returns a new set containing elements common to both sets.

```python
candy_bars = {"Milky Way", "Snickers"}
sweet_things = {"Sour Patch Kids", "Snickers"}
print(candy_bars.intersection(sweet_things))  # Output: {'Snickers'}
```

---

## 7. The `difference` Method
File: [the-difference-method.py](17-sets/the-difference-method.py)

The `difference` method returns a new set containing elements in one set but not in the other.

```python
candy_bars = {"Milky Way", "Snickers"}
sweet_things = {"Sour Patch Kids", "Snickers"}
print(candy_bars.difference(sweet_things))  # Output: {'Milky Way'}
```

---

## 8. The `symmetric_difference` Method
File: [the-symmetric-difference.py](17-sets/the-symmetric-difference.py)

The `symmetric_difference` method returns a new set containing elements that are in either set but not in both.

```python
candy_bars = {"Milky Way", "Snickers"}
sweet_things = {"Sour Patch Kids", "Snickers"}
print(candy_bars.symmetric_difference(sweet_things))  # Output: {'Milky Way', 'Sour Patch Kids'}
```

---

## 9. The `issubset` and `issuperset` Methods
File: [the-issubset-and-issuperset-method.py](17-sets/the-issubset-and-issuperset-method.py)

The `issubset` method checks if all elements of one set are in another set. The `issuperset` method checks if a set contains all elements of another set.

```python
a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))  # Output: True
print(b.issuperset(a))  # Output: True
```

---

## 10. The `frozenset` Object
File: [the-frozenset-object.py](17-sets/the-frozenset-object.py)

A `frozenset` is an immutable version of a set. It cannot be modified after creation.

```python
mr_freeze = frozenset([1, 2, 3])
print(mr_freeze)  # Output: frozenset({1, 2, 3})
```

---


## 11. Practice Problems
File: [assignment.py](17-sets/assignment.py)

This section focuses on solving practical problems using sets. Below are some examples:



### 11.1. Remove Duplicates
The `remove_duplicates` function accepts a list and returns a new list with all duplicate elements removed. The order of elements in the returned list is irrelevant because sets are unordered.

```python
def remove_duplicates(elements):
    return list(set(elements))

print(remove_duplicates([1, 2, 2, 1]))  # Output: [1, 2]
print(remove_duplicates(["apple", "banana", "apple", "orange"]))  # Output: ['apple', 'banana', 'orange']
print(remove_duplicates([]))  # Output: []
```

**Key Insights:**
- Sets automatically remove duplicates, making them ideal for this task.
- Converting a set back to a list ensures the output is in list format.

---

### 11.2. Create a Set of Movies
This exercise demonstrates how to create a set of unique movie titles. Sets are useful for ensuring no duplicate entries exist.

```python
movies = {"Inception", "American Gangster", "Heat"}
print(movies)  # Output: {'Inception', 'American Gangster', 'Heat'}

# Adding more movies to the set
movies.add("The Dark Knight")
movies.add("Inception")  # Duplicate, will not be added
print(movies)  # Output: {'Inception', 'American Gangster', 'Heat', 'The Dark Knight'}
```

**Key Insights:**
- Sets automatically prevent duplicate entries.
- The `add` method is used to add individual elements to a set.

---

### 11.3. Find Common Elements Between Two Sets
This exercise demonstrates how to find the intersection of two sets, which includes elements common to both sets.

```python
set_a = {"apple", "banana", "cherry"}
set_b = {"banana", "cherry", "date", "fig"}

common_elements = set_a.intersection(set_b)
print(common_elements)  # Output: {'banana', 'cherry'}
```

**Key Insights:**
- The `intersection` method or `&` operator can be used to find common elements between sets.

---

### 11.4. Find Unique Elements in One Set
This exercise demonstrates how to find elements that are in one set but not in another using the `difference` method.

```python
set_a = {"apple", "banana", "cherry"}
set_b = {"banana", "cherry", "date", "fig"}

unique_to_a = set_a.difference(set_b)
print(unique_to_a)  # Output: {'apple'}
```

**Key Insights:**
- The `difference` method or `-` operator can be used to find elements unique to one set.

---

### 11.5. Combine Two Sets Without Duplicates
This exercise demonstrates how to combine two sets into one, ensuring no duplicates exist, using the `union` method.

```python
set_a = {"apple", "banana", "cherry"}
set_b = {"banana", "cherry", "date", "fig"}

combined_set = set_a.union(set_b)
print(combined_set)  # Output: {'apple', 'banana', 'cherry', 'date', 'fig'}
```

**Key Insights:**
- The `union` method or `|` operator can be used to combine sets while removing duplicates.

---

### 11.6. Check Subset and Superset Relationships
This exercise demonstrates how to check if one set is a subset or superset of another.

```python
set_a = {"apple", "banana"}
set_b = {"apple", "banana", "cherry"}

print(set_a.issubset(set_b))  # Output: True
print(set_b.issuperset(set_a))  # Output: True
```

**Key Insights:**
- The `issubset` and `issuperset` methods are useful for checking hierarchical relationships between sets.

---

### 11.7. Use a `frozenset` for Immutable Sets
This exercise demonstrates how to use a `frozenset` to create an immutable set.

```python
immutable_set = frozenset(["apple", "banana", "cherry"])
print(immutable_set)  # Output: frozenset({'apple', 'banana', 'cherry'})

# Attempting to modify the frozenset will raise an error
# immutable_set.add("date")  # AttributeError: 'frozenset' object has no attribute 'add'
```

**Key Insights:**
- `frozenset` is useful when you need a set that cannot be modified, such as for use as a dictionary key.

---

### 11.8. Count Unique Elements in a List
This exercise demonstrates how to count the number of unique elements in a list using a set.

```python
elements = [1, 2, 2, 3, 4, 4, 5]
unique_count = len(set(elements))
print(unique_count)  # Output: 5
```

**Key Insights:**
- Converting a list to a set removes duplicates, making it easy to count unique elements.

---

### 11.9. Generate a Set of Squares
This exercise demonstrates how to use a set comprehension to generate a set of squares.

```python
numbers = [-3, -2, -1, 0, 1, 2, 3]
squares = {number ** 2 for number in numbers}
print(squares)  # Output: {0, 1, 4, 9}
```

**Key Insights:**
- Set comprehensions provide a concise way to create sets based on a condition or transformation.

---

### 11.10. Remove Elements from a Set
This exercise demonstrates how to remove elements from a set using the `discard` method.

```python
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
fruits.discard("date")  # No error if the element is not found
print(fruits)  # Output: {'apple', 'cherry'}
```

**Key Insights:**
- The `discard` method is safer than `remove` because it does not raise an error if the element is not found.

---

## Summary

Through these exercises, I gained a deeper understanding of:
- Using sets for tasks like removing duplicates, finding common or unique elements, and combining collections.
- Leveraging set methods like `union`, `intersection`, `difference`, and `symmetric_difference`.
- Working with immutable sets using `frozenset`.
- Applying set comprehensions for concise and efficient set creation.

Sets are a versatile and powerful data structure for managing unique collections and performing mathematical operations in Python.