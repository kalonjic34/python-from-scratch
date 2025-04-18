print(" -  Coding Exercise - date and time Objects\n")

# 1. Declare a `titanic` variable pointing to a date object representing April 14th, 1912.
# 2. Declare an `independence_day` variable pointing to a date object representing July 4th, 1776.
# 3. Declare an `alarm_clock` variable set to a time object representing 08:45:00 AM.
# 4. Declare a `one_second_away` variable set to a time object representing 11:59:59 PM.

from datetime import time
from datetime import date

titanic = date(year=1912,month=4,day=14)
print(titanic)

independence_day = date(1776,7,4)
print(independence_day)

alarm_clock = time(hour=5,minute=45,second=00)
print(alarm_clock)

one_second_away = time(23,59,59)
print(one_second_away)

print("\n - Coding Exercise SOLUTION The datetime Object\n")

# Define a function named `one_from_two` that accepts a date object and a time object.
# - The function should return a datetime object consisting of:
#   - The year, month, and day from the date object.
#   - The hour, minutes, and seconds from the time object.

# Example usage:
# from datetime import date, time, datetime

# some_date = date(2002, 2, 22)
# some_time = time(9, 45, 23)

# one_from_two(some_date, some_time) => datetime object representing 2002-02-22 09:45:23

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