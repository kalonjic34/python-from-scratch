# import datetime
from datetime import date

birthday = date(2000,4,15)
print(birthday)
print(type(birthday))


moon_landing = date(year=1969, month=7, day=20)
print(moon_landing)

# date(2025, 15, 10) # ValueError: month must be in 1..12
# date(2020,1,35) # ValueError: day is out of range for month

print(birthday.year)
print(birthday.month)
print(birthday.day)

# birthday.year = 1999 #AttributeError: attribute 'year' of 'datetime.date' objects is not writable

today = date.today()
print(today)
print(type(today))