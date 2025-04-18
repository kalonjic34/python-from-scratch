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