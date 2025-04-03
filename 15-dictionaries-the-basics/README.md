# Dictionaries: The Basics

This document provides a detailed summary of the key concepts and lessons I learned while exploring dictionaries in Python. Dictionaries are powerful data structures that store key-value pairs, allowing for efficient data retrieval and manipulation. Below is a breakdown of the topics covered and the insights gained.

---

## 1. Introduction to Dictionaries
File: [intro-to-dictionaries.py](15-dictionaries-the-basics/intro-to-dictionaries.py)

Dictionaries store data as key-value pairs and allow for quick access to values using their keys.

```python
ice_cream_preferences = {
    "Benjamin": "Chocolate",
    "Samantha": "Vanilla",
    "Marv": "Cookies & Creme",
    "Julia": "Chocolate"
}

print(len(ice_cream_preferences))  # Output: 4
```

---

## 2. Accessing Dictionary Values
File: [access-a-dictionary-value-by-key-or-the-get-method.py](15-dictionaries-the-basics/access-a-dictionary-value-by-key-or-the-get-method.py)

You can access dictionary values using keys or the `get` method, which provides a default value if the key is not found.

```python
flight_prices = {
    "Chicago": 199,
    "San Francisco": 499,
    "Denver": 295
}

print(flight_prices["Chicago"])  # Output: 199
print(flight_prices.get("Seattle", "Price not available"))  # Output: Price not available
```

---

## 3. Adding or Modifying Key-Value Pairs
File: [add-or-modify-key-value-pair-in-dictionary.py](15-dictionaries-the-basics/add-or-modify-key-value-pair-in-dictionary.py)

You can add new key-value pairs or modify existing ones in a dictionary.

```python
sports_team_rosters = {
    "New England Patriots": ["Tom Brady", "Rob Gronkowski"],
    "New York Giants": ["Eli Manning"]
}

sports_team_rosters["Pittsburg Steelers"] = ["Ben Rothlisberger"]
sports_team_rosters["New York Giants"] = ["Eli Manning", "Odell Beckham"]
print(sports_team_rosters)
```

---

## 4. The `in` and `not in` Operators
File: [the-in-and-not-in-operators-on-a-dictionary.py](15-dictionaries-the-basics/the-in-and-not-in-operators-on-a-dictionary.py)

The `in` and `not in` operators check for the presence of keys in a dictionary.

```python
pokemon = {
    "Fire": ["Charmander", "Charmeleon"],
    "Water": ["Squirtle", "Wartortle"],
    "Grass": ["Bulbasaur", "Ivysaur"]
}

print("Fire" in pokemon)  # Output: True
print("Electric" not in pokemon)  # Output: True
```

---

## 5. The `setdefault` Method
File: [the-setdefault-method.py](15-dictionaries-the-basics/the-setdefault-method.py)

The `setdefault` method retrieves a value for a key or sets it to a default value if the key does not exist.

```python
film_directors = {
    "The Godfather": "Francis Ford Coppola",
    "The Rock": "Michael Bay"
}

film_directors.setdefault("Bad Boys", "Michael Bay")
print(film_directors)
```

---

## 6. The `pop` Method
File: [the-pop-method.py](15-dictionaries-the-basics/the-pop-method.py)

The `pop` method removes a key-value pair from a dictionary and returns the value.

```python
release_dates = {
    "Python": 1991,
    "Ruby": 1995
}

year = release_dates.pop("Ruby")
print(year)  # Output: 1995
print(release_dates)  # Output: {'Python': 1991}
```

---

## 7. The `clear` Method
File: [the-clear-method.py](15-dictionaries-the-basics/the-clear-method.py)

The `clear` method removes all key-value pairs from a dictionary, leaving it empty.

```python
websites = {
    "Wikipedia": "http://www.wikipedia.org",
    "Google": "http://www.google.com"
}

websites.clear()
print(websites)  # Output: {}
```

---

## 8. The `update` Method
File: [the-update-method.py](15-dictionaries-the-basics/the-update-method.py)

The `update` method merges another dictionary into the current dictionary, overwriting existing keys.

```python
employee_salaries = {
    "Guido": 100000,
    "James": 500000
}

extra_salaries = {
    "Yukihiro": 1000000,
    "Guido": 333333
}

employee_salaries.update(extra_salaries)
print(employee_salaries)
```

---

## 9. The `dict` Function
File: [the-dict-function.py](15-dictionaries-the-basics/the-dict-function.py)

The `dict` function creates a dictionary from a list of key-value pairs.

```python
employee_titles = [
    ["Mary", "Senior Manager"],
    ["Brian", "Vice President"]
]

print(dict(employee_titles))
```

---

## 10. Nested Dictionaries
File: [nested-dictionaries.py](15-dictionaries-the-basics/nested-dictionaries.py)

Dictionaries can contain other dictionaries, allowing for hierarchical data structures.

```python
tv_shows = {
    "The X-Files": {
        "Season 1": {
            "Episodes": ["Scary Monster", "Scary Alien"],
            "Year": 1993
        }
    }
}

print(tv_shows["The X-Files"]["Season 1"]["Episodes"][1])  # Output: Scary Alien
```

---

## 11. Practice Problems
File: [assignment.py](15-dictionaries-the-basics/assignment.py)

This section focuses on solving practical problems using dictionaries. Below are some examples:

### 11.1. Convert List to Dictionary
```python
def to_dictionary(elements):
    return {element: index for index, element in enumerate(elements)}

print(to_dictionary(["Sherlock Holmes", "Nancy Drew"]))
```

### 11.2. Count String Lengths
```python
def length_counts(elements):
    counts = {}
    for element in elements:
        length = len(element)
        counts[length] = counts.get(length, 0) + 1
    return counts

print(length_counts(["Brazil", "Peru", "Venezuela"]))
```

---

## Summary

Through these exercises, I gained a comprehensive understanding of:
- Creating, accessing, and modifying dictionaries.
- Using dictionary methods like `setdefault`, `pop`, `clear`, and `update`.
- Working with nested dictionaries for hierarchical data.
- Solving practical problems using dictionaries.

Dictionaries are versatile and essential for efficient data management in Python.