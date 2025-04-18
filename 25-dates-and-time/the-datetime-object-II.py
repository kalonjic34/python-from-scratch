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