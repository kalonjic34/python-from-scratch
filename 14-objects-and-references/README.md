# Objects and References

This document provides a detailed summary of the key concepts and lessons I learned while exploring objects and references in Python. Understanding how Python handles variables, objects, and memory is crucial for writing efficient and bug-free code. Below is a breakdown of the topics covered and the insights gained.

---

## 1. Variables, Objects, and Garbage Collection
File: [variables-objects-and-garbage-collection.py](14-objects-and-references/variables-objects-and-garbage-collection.py)

This script demonstrates how variables in Python reference objects and how reassignment makes objects eligible for garbage collection.

```python
a = 3
a = 10  # The integer 3 is now eligible for garbage collection
a = "hello"  # The integer 10 is now eligible for garbage collection
a = [1, 2, 3]  # The string "hello" is now eligible for garbage collection
a = [4, 5, 6]  # The list [1, 2, 3] is now eligible for garbage collection
```

---

## 2. Shared References with Immutable and Mutable Types
File: [shared-references-with-immutable-and-mutable-types.py](14-objects-and-references/shared-references-with-immutable-and-mutable-types.py)

This script explores how shared references behave differently for immutable and mutable types.

```python
# Immutable types
a = 3
b = a
a = 5
print(a)  # Output: 5
print(b)  # Output: 3

# Mutable types
a = [1, 2, 3]
b = a
a.append(4)
print(a)  # Output: [1, 2, 3, 4]
print(b)  # Output: [1, 2, 3, 4]
```

---

## 3. Equality vs. Identity
File: [equality-vs-identity.py](14-objects-and-references/equality-vs-identity.py)

This script demonstrates the difference between equality (`==`) and identity (`is`) in Python.

```python
students = ["James", "Sam", "Alice"]
athletes = students
nerds = ["James", "Sam", "Alice"]

print(students == nerds)  # Output: True (values are equal)
print(students is nerds)  # Output: False (different objects in memory)
```

---

## 4. Shallow and Deep Copies
File: [shallow-and-deep-copies.py](14-objects-and-references/shallow-and-deep-copies.py)

This script explains the difference between shallow and deep copies using slicing, the `copy` module, and the `deepcopy` method.

```python
import copy

a = [1, [2, 3], 4]
b = copy.copy(a)  # Shallow copy
c = copy.deepcopy(a)  # Deep copy

a[1].append(100)
print(b)  # Output: [1, [2, 3, 100], 4] (shallow copy affected)
print(c)  # Output: [1, [2, 3], 4] (deep copy unaffected)
```

---

## Summary

I gained a comprehensive understanding of:
- How Python handles variables and objects in memory.
- The difference between equality and identity.
- The behavior of shared references for mutable and immutable types.
- The distinction between shallow and deep copies.

These concepts are fundamental for writing efficient and predictable Python code.