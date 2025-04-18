from datetime import datetime, timedelta

birthday = datetime(2000, 4, 15)
today = datetime.now()

my_life_span = today - birthday
print(my_life_span)
print(type(my_life_span))

print(my_life_span.total_seconds())

five_hundred_days = timedelta(days = 500, hours = 12)
print(five_hundred_days)

print(five_hundred_days + five_hundred_days)