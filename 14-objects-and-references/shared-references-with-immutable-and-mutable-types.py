"""
This script demonstrates the behavior of shared references with immutable and mutable types in Python.

1. Immutable types (e.g., integers):
    - `a` is assigned the value 3.
    - `b` is assigned the value of `a` (both point to the same integer object initially).
    - When `a` is reassigned to 5, it points to a new integer object, leaving `b` unchanged.

2. Mutable types (e.g., lists):
    - `a` is assigned a list `[1, 2, 3]`.
    - `b` is assigned the reference of `a` (both point to the same list object).
    - Modifying the list through `a` (e.g., appending 4) affects both `a` and `b` since they share the same reference.
    - Similarly, modifying the list through `b` (e.g., appending 5) also affects both `a` and `b`.
"""

a = 3
b = a

a = 5

print(a)
print(b)

a = [1,2,3]
b = a

a.append(4)
print(a)
print(b)

b.append(5)

print(a)
print(b)