import time
import datetime
import calendar
import pytz

# print(time.time()) # epoch time
# print(time.ctime()) # human readable time

# t1 = datetime.datetime.now()
# print(t1)
# print("Hello")
# t2 = datetime.datetime.now()
# print(t2)

# t = t2-t1

# print(t)

#print(calendar.month(2021,6))

print(datetime.datetime.now(pytz.timezone("US/Eastern")))