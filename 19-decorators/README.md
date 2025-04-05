# Decorators

This document provides a detailed summary of the key concepts and lessons I learned while exploring decorators in Python. Decorators are a powerful feature that allows us to modify or extend the behavior of functions or methods. Below is a breakdown of the topics covered and the insights gained.

---

## 1. Introduction to Decorators
File: [intro-to-decorators.py](19-decorators/intro-to-decorators.py)

Decorators are functions that take another function as input and return a new function with modified or extended behavior.

```python
def be_nice(fn):
    def inner():
        print("Nice to meet you! I'm honored to execute your function for you!")
        fn()
        print("It was my pleasure executing your function! Have a nice day!")
    return inner

@be_nice
def complex_business_logic():
    print("Something complex!")

complex_business_logic()
```

---

## 2. Arguments with Decorator Functions
File: [arguments-with-decorator-functions.py](19-decorators/arguments-with-decorator-functions.py)

Decorators can accept arguments using `*args` and `**kwargs` to handle functions with varying parameters.

```python
def be_nice(fn):
    def inner(*args, **kwargs):
        print("Nice to meet you! I'm honored to execute your function for you!")
        fn(*args, **kwargs)
        print("It was my pleasure executing your function! Have a nice day!")
    return inner

@be_nice
def complex_business_logic(stakeholder, position):
    print(f"Something complex for {position} {stakeholder}!")

complex_business_logic("Christian", "CEO")
```

---

## 3. Returned Values from Decorated Functions
File: [returned-values-from-decorated-functions.py](19-decorators/returned-values-from-decorated-functions.py)

Decorators can return values from the wrapped function by capturing the result and returning it.

```python
def be_nice(fn):
    def inner(*args, **kwargs):
        print("Nice to meet you! I'm honored to execute your function for you!")
        result = fn(*args, **kwargs)
        print("It was my pleasure executing your function! Have a nice day!")
        return result
    return inner

@be_nice
def complex_business_sum(a, b):
    return a + b

print(complex_business_sum(3, 5))  # Output: 8
```

---

## 4. The `functools.wraps` Decorator
File: [the-functools-wraps-decorator.py](19-decorators/the-functools-wraps-decorator.py)

The `functools.wraps` decorator preserves the metadata (e.g., docstrings and function names) of the original function when it is wrapped by a decorator.

```python
import functools

def be_nice(fn):
    @functools.wraps(fn)
    def inner(*args, **kwargs):
        print("Nice to meet you! I'm honored to execute your function for you!")
        result = fn(*args, **kwargs)
        print("It was my pleasure executing your function! Have a nice day!")
        return result
    return inner

@be_nice
def complex_business_sum(a, b):
    """Adds two numbers together."""
    return a + b

help(complex_business_sum)
```

---

## 5. Nested Functions
File: [nested-functions.py](19-decorators/nested-functions.py)

Nested functions are functions defined inside other functions. They are often used in decorators to encapsulate logic.

```python
def convert_gallons_to_cups(gallons):
    def gallons_to_quarts(gallons):
        return gallons * 4
    def quarts_to_pints(quarts):
        return quarts * 2
    def pints_to_cups(pints):
        return pints * 2

    quarts = gallons_to_quarts(gallons)
    pints = quarts_to_pints(quarts)
    return pints_to_cups(pints)

print(convert_gallons_to_cups(1))  # Output: 16
```

---

## 6. Higher-Order Functions
File: [higher-order-functions-I.py](19-decorators/higher-order-functions-I.py)

Higher-order functions are functions that accept other functions as arguments or return functions as results.

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def calculate(func, a, b):
    return func(a, b)

print(calculate(add, 10, 24))  # Output: 34
print(calculate(subtract, 8, 14))  # Output: -6
```

---

## 7. Closures
File: [scope-III-closures.py](19-decorators/scope-III-closures.py)

Closures are functions that retain access to variables from their enclosing scope, even after the enclosing scope has finished executing.

```python
def outer():
    candy = "Snickers"
    def inner():
        return candy
    return inner

the_func = outer()
print(the_func())  # Output: Snickers
```

---

## 8. The `nonlocal` Keyword
File: [the-nonlocal-keyword.py](19-decorators/the-nonlocal-keyword.py)

The `nonlocal` keyword allows you to modify variables in an enclosing (non-global) scope.

```python
def outer():
    flavor = "Black"
    def inner():
        nonlocal flavor
        flavor = "Taro"
    inner()
    return flavor

print(outer())  # Output: Taro
```

---

## 9. The `global` Keyword
File: [the-global-keyword.py](19-decorators/the-global-keyword.py)

The `global` keyword allows you to modify variables in the global scope.

```python
x = 10

def change_stuff():
    global x
    x = 15

change_stuff()
print(x)  # Output: 15
```

---

## 10. Practice Problems
File: [assignment.py](19-decorators/assignment.py)

This section focuses on solving practical problems using decorators. Below are some examples:

### 10.1. Invoke a Function Three Times
The `invoke_thrice` function accepts another function as an argument and invokes it exactly three times. This demonstrates how functions can be passed as arguments and executed dynamically.

```python
def invoke_thrice(func):
    func()
    func()
    func()

def sample():
    print("A")
    print("B")
    print("C")

invoke_thrice(sample)
```

**Key Insights:**
- Functions in Python are first-class objects, meaning they can be passed as arguments to other functions.
- This exercise highlights the flexibility of Python functions and their ability to be reused dynamically.

---

### 10.2. Return a Function from Another Function
The `outer` function defines an `inner` function and returns it without invoking it. This demonstrates the concept of closures, where a function retains access to variables in its enclosing scope.

```python
def outer():
    def inner():
        return 5
    return inner

print(outer()())  # Output: 5
```

**Key Insights:**
- Functions can be defined inside other functions and returned for later use.
- Closures allow inner functions to retain access to variables in their enclosing scope, even after the outer function has finished executing.

---

### 10.3. Modify a Global Variable
The `modify_a` function demonstrates how to modify a global variable using the `global` keyword. This is useful when you need to update a variable defined outside the function's scope.

```python
a = 1

def modify_a(value):
    global a
    a = value

print(a)  # Output: 1
modify_a(10)
print(a)  # Output: 10
```

**Key Insights:**
- The `global` keyword allows functions to modify variables defined in the global scope.
- Use the `global` keyword sparingly, as it can make code harder to debug and maintain.

---

## Summary

Through these exercises, I gained a deeper understanding of:
- Using decorators to modify or extend function behavior.
- Leveraging higher-order functions and closures for dynamic and reusable code.
- Applying the `global` and `nonlocal` keywords to modify variables in different scopes.
- Preserving function metadata with `functools.wraps`.

Decorators and related concepts are powerful tools for writing flexible, reusable, and maintainable Python code.