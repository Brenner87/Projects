import datetime
from datetime import date, timedelta


a = datetime.date.today()
#print(a)

my_date = datetime.date(year=a.year, month=a.month, day=1)
# print(my_date)
# print(datetime.timedelta(a.year,a.month))
# print(a<my_date)


my_date='2020-03-06'
a=datetime.datetime.strptime(my_date, '%Y-%m-%d')
a=datetime.datetime.date(a)
print(type(a))

print(isinstance(a, datetime.date))

prev_date=a.replace(day=1)-timedelta(days=1)
print(prev_date.month, prev_date.year)