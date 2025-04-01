# List: Mutation

This document provides a detailed summary of the key concepts and lessons I learned while exploring list mutation in Python. Lists are mutable, meaning their elements can be changed, added, or removed after creation. Below is a breakdown of the topics covered and the insights gained.

---

## 1. Assigning a New Value at an Index
File: [assign-new-value-at-index.py](10-list-mutation/assign-new-value-at-index.py)

I learned how to overwrite the value at a specific index in a list.

```python
crayons = ["Macaroni and Cheese", "Maximum Yellow Red", "Jazzberry Jam"]
crayons[1] = "Cotton Candy"
print(crayons)  # Output: ['Macaroni and Cheese', 'Cotton Candy', 'Jazzberry Jam']
```

---

## 2. Assigning New Values to a List Slice
File: [assign-new-values-to-list-slice.py](10-list-mutation/assign-new-values-to-list-slice.py)

I explored how to replace multiple elements in a list using slicing.

```python
coworkers = ["Michael", "Jim", "Dwight", "Pam", "Creed", "Angela"]
coworkers[3:5] = ["Oscar", "Ryan"]
print(coworkers)  # Output: ['Michael', 'Jim', 'Dwight', 'Oscar', 'Ryan', 'Angela']
```

---

## 3. The `append` Method
File: [the-append-method.py](10-list-mutation/the-append-method.py)

The `append` method adds a single element to the end of a list.

```python
countries = ["United States", "Canada", "Australia"]
countries.append("Japan")
print(countries)  # Output: ['United States', 'Canada', 'Australia', 'Japan']
```

---

## 4. The `extend` Method
File: [the-extend-method.py](10-list-mutation/the-extend-method.py)

The `extend` method adds all elements from another list to the end of the current list.

```python
mountains = ["Mount Everest", "K2"]
mountains.extend(["Kangchenjunga", "Lhotse", "Makalu"])
print(mountains)  # Output: ['Mount Everest', 'K2', 'Kangchenjunga', 'Lhotse', 'Makalu']
```

---

## 5. The `insert` Method
File: [the-insert-method.py](10-list-mutation/the-insert-method.py)

The `insert` method adds an element at a specific index in a list.

```python
plays = ["Hamlet", "Macbeth", "King Lear"]
plays.insert(1, "Julius Caesar")
print(plays)  # Output: ['Hamlet', 'Julius Caesar', 'Macbeth', 'King Lear']
```

---

## 6. The `pop` Method
File: [the-pop-method.py](10-list-mutation/the-pop-method.py)

The `pop` method removes and returns an element at a specific index. If no index is provided, it removes the last element.

```python
action_stars = ["Norris", "Seagal", "Van Damme", "Washington"]
last_action_hero = action_stars.pop()
print(last_action_hero)  # Output: Washington
```

---

## 7. The `del` Keyword
File: [the-del-keyword.py](10-list-mutation/the-del-keyword.py)

The `del` keyword removes elements from a list by index or slice.

```python
soups = ["French Onion", "Clam Chowder", "Chicken Noodle", "Wonton"]
del soups[1:3]
print(soups)  # Output: ['French Onion', 'Wonton']
```

---

## 8. The `remove` Method
File: [the-remove-method.py](10-list-mutation/the-remove-method.py)

The `remove` method removes the first occurrence of a specified value from a list.

```python
nintendo_games = ["Zelda", "Mario", "Donkey Kong", "Zelda"]
nintendo_games.remove("Zelda")
print(nintendo_games)  # Output: ['Mario', 'Donkey Kong', 'Zelda']
```

---

## 9. The `clear` Method
File: [the-clear-method.py](10-list-mutation/the-clear-method.py)

The `clear` method removes all elements from a list, leaving it empty.

```python
citrus_fruits = ["Lemon", "Orange", "Lime"]
citrus_fruits.clear()
print(citrus_fruits)  # Output: []
```

---

## 10. The `reverse` Method
File: [the-reverse-method.py](10-list-mutation/the-reverse-method.py)

The `reverse` method reverses the order of elements in a list.

```python
vitamins = ["A", "D", "K"]
vitamins.reverse()
print(vitamins)  # Output: ['K', 'D', 'A']
```

---

## 11. The `sort` Method
File: [the-sort-method.py](10-list-mutation/the-sort-method.py)

The `sort` method sorts the elements of a list in ascending order. The `sorted` function can be used to create a sorted copy without modifying the original list.

```python
temperatures = [40, 20, 52, 66, 35]
temperatures.sort()
print(temperatures)  # Output: [20, 35, 40, 52, 66]
```

---

## 12. Building a List from Another List
File: [building-a-list-up-from-another-list.py](10-list-mutation/building-a-list-up-from-another-list.py)

I learned how to create new lists by transforming elements from an existing list.

```python
def squares(numbers):
    return [number ** 2 for number in numbers]

print(squares([1, 2, 3]))  # Output: [1, 4, 9]
```

---

## 13. Practice Problems
File: [assignment.py](10-list-mutation/assignment.py)

This section focuses on solving practical problems using list mutation. Below are the functions I implemented:

### 13.1. Overwriting Elements
```python
great_directors = ["Martin Scorsese", "Steven Spielberg", "Francis Ford Coppola"]
great_directors[1] = "Michael Bay"
print(great_directors)  # Output: ['Martin Scorsese', 'Michael Bay', 'Francis Ford Coppola']
```

---

### 13.2. Filtering Even Numbers
```python
def only_evens(numbers):
    return [number for number in numbers if number % 2 == 0]

print(only_evens([4, 8, 15, 16, 23, 42]))  # Output: [4, 8, 16, 42]
```

---

### 13.3. Removing All Occurrences
```python
def delete_all(items, target):
    while target in items:
        items.remove(target)
    return items

print(delete_all(["apple", "banana", "apple", "cherry"], "apple"))  # Output: ['banana', 'cherry']
```

---

### 13.4. Finding Factors
```python
def factors(number):
    return [i for i in range(1, number + 1) if number % i == 0]

print(factors(10))  # Output: [1, 2, 5, 10]
```

---

### 13.5. Push or Pop
```python
def push_or_pop(numbers):
    result = []
    for number in numbers:
        if number > 5:
            result.append(number)
        elif number <= 5 and result:
            result.pop()
    return result

print(push_or_pop([10, 4, 6]))  # Output: [10, 6]
```

---

## Summary

Through these exercises, I gained a comprehensive understanding of list mutation in Python, including:
- Modifying elements and slices.
- Adding, removing, and reordering elements.
- Building new lists from existing ones.
- Solving practical problems using list mutation.

These skills are essential for working with dynamic data structures in Python.