from datetime import datetime

print(datetime(1999,7,24))
print(datetime(1999,7,24, 14))
print(datetime(1999,7,24, 14,16))
print(datetime(1999,7,24, 14,16,58))

print(datetime(year=1999,month=7,day=24, hour=14, minute=16,second=58))

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

same_time_twenty_years_ago = today.replace(year = 2000)
print(same_time_twenty_years_ago)

same_time_twenty_years_ago = today.replace(month= 1)
print(same_time_twenty_years_ago)

start_of_january_2000 = today.replace(year=2000, month=1, day= 1)
print(start_of_january_2000)