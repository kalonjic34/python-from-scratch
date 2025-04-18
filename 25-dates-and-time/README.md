# README: Date and Time Handling in Python

This document summarizes key concepts and examples related to handling date and time in Python. Proper management of date and time is essential for many applications, from scheduling to logging and beyond.

---

## 1. The Time Object
**File:** [the-time-object.py](the-time-object.py)

In this example, I demonstrate the creation and manipulation of time objects using the `datetime` module.

```python
from datetime import time

start = time()
print(start)
print(type(start))
print(start.hour)
print(start.minute)
print(start.second)

print(time(6))
print(time(hour=6))
print(time(hour=18))

print(time(12, 25))
print(time(hour=12, minute=25))

# 11:34:22 PM
print(time(23, 34, 22))
evening = time(hour=23, minute=34, second=22)
print(evening.hour)
print(evening.minute)
print(evening.hour)
```

**Key Insights:**
- The `time` object represents **only the time** (hours, minutes, seconds) without any date component.
- I can instantiate `time` objects with various parameters for greater flexibility in defining time values.

---

## 2. The Timedelta Object
**File:** [the-timedelta-object.py](the-timedelta-object.py)

In this example, I illustrate how to use the `timedelta` object to perform date and time arithmetic.

```python
from datetime import datetime, timedelta

birthday = datetime(2000, 4, 15)
today = datetime.now()

my_life_span = today - birthday
print(my_life_span)
print(type(my_life_span))

print(my_life_span.total_seconds())

five_hundred_days = timedelta(days=500, hours=12)
print(five_hundred_days)

print(five_hundred_days + five_hundred_days)
```

**Key Insights:**
- The `timedelta` object represents a duration, allowing me to perform arithmetic operations on `datetime` objects.
- I can calculate differences between dates and create durations to manipulate date and time easily.

---

## 3. The Datetime Object II
**File:** [the-datetime-object-II.py](the-datetime-object-II.py)

In this example, I show how to format `datetime` objects using `strftime`.

```python
from datetime import datetime

today = datetime.today()

print(today.strftime("%m"))
print(today.strftime("%m %d"))
print(today.strftime("%m-%d-%Y"))
print(today.strftime("%m/%d/%Y"))

print(today.strftime("%Y-%m-%d"))
print(today.strftime("%y-%m-%d"))

print(today.strftime("%A"))
print(today.strftime("%B"))
```

**Key Insights:**
- The `strftime` method allows me to **format `datetime` objects** as strings in various styles, which is useful for displaying dates in user-friendly formats.
- This flexibility is essential for applications that require specific date formats for reporting or user interfaces.

---

## 4. The Datetime Object I
**File:** [the-datetime-object-I.py](the-datetime-object-I.py)

In this example, I demonstrate the creation of `datetime` objects and how to access their attributes.

```python
from datetime import datetime

print(datetime(1999, 7, 24))
print(datetime(1999, 7, 24, 14))
print(datetime(1999, 7, 24, 14, 16))
print(datetime(1999, 7, 24, 14, 16, 58))

print(datetime(year=1999, month=7, day=24, hour=14, minute=16, second=58))

today = datetime.today()
print(today)
print(datetime.now())
print(today.year)
print(today.month)
print(today.day)
print(today.hour)
print(today.minute)
print(today.second)

print(today.weekday())

same_time_twenty_years_ago = today.replace(year=2000)
print(same_time_twenty_years_ago)

same_time_twenty_years_ago = today.replace(month=1)
print(same_time_twenty_years_ago)

start_of_january_2000 = today.replace(year=2000, month=1, day=1)
print(start_of_january_2000)
```

**Key Insights:**
- The `datetime` object contains both **date and time** information, providing a comprehensive representation of a specific moment in time.
- I can access various attributes of the `datetime` object, such as year, month, and day, for easy manipulation and analysis.

---

## 5. The Date Object
**File:** [the-date-object.py](the-date-object.py)

In this example, I illustrate the creation and manipulation of date objects.

```python
# import datetime
from datetime import date

birthday = date(2000, 4, 15)
print(birthday)
print(type(birthday))

moon_landing = date(year=1969, month=7, day=20)
print(moon_landing)

# date(2025, 15, 10) # ValueError: month must be in 1..12
# date(2020, 1, 35)  # ValueError: day is out of range for month

print(birthday.year)
print(birthday.month)
print(birthday.day)

# birthday.year = 1999 #AttributeError: attribute 'year' of 'datetime.date' objects is not writable

today = date.today()
print(today)
print(type(today))
```

**Key Insights:**
- The `date` object represents **only the date** (year, month, day) without any time component.
- Attempting to set attributes like `year` directly will raise an `AttributeError`, highlighting that `date` objects are immutable.

---

## 6. Assignment: Date and Time Objects

### 6.1 - Date and Time Objects
**File:** [assignment.py](assignment.py)

In this part, I create date and time objects.

```python
print(" -  Coding Exercise - date and time Objects\n")

from datetime import time
from datetime import date

titanic = date(year=1912, month=4, day=14)
print(titanic)

independence_day = date(1776, 7, 4)
print(independence_day)

alarm_clock = time(hour=5, minute=45, second=0)
print(alarm_clock)

one_second_away = time(23, 59, 59)
print(one_second_away)
```

### 6.2 - The Datetime Object
In this part, I define a function to combine date and time into a datetime object.

```python
print("\n - Coding Exercise SOLUTION The datetime Object\n")

from datetime import datetime, date, time 

def one_from_two(some_date, some_time):
    year = some_date.year
    month = some_date.month
    day = some_date.day
    
    hour = some_time.hour
    minute = some_time.minute
    second = some_time.second
    
    return datetime(year, month, day, hour, minute, second)

some_date = date(2002, 2, 22)
some_time = time(9, 45, 23)
result = one_from_two(some_date, some_time)

print(result)
```

**Key Insights:**
- This exercise demonstrates how to create and manipulate `date` and `time` objects, emphasizing their individual components.
- The function `one_from_two` effectively combines `date` and `time` objects into a single `datetime` object, showcasing the interoperability of these components in Python.

---

## Summary

Through these exercises, I gained a comprehensive understanding of:
- The creation and manipulation of `time`, `date`, and `datetime` objects.
- The use of `timedelta` for date arithmetic.
- Formatting dates and times using `strftime`.
- Implementing functions that combine `date` and `time` into `datetime`.

These concepts are essential for managing date and time effectively in Python applications.