#!/usr/bin/env python3
# date time
from datetime import datetime

now = datetime.now()

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

timestamp = now.timestamp()
print(timestamp)

year_2024 = datetime(
    2023,
    1,
    1,
)


def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())


print_date(now)

print_date(year_2024)

from datetime import time

current_time = time()

print(current_time)

from datetime import date

current_date = date.today()

print(current_date)

current_date = date(current_date.year, current_date.month, current_date.day)
print(current_date)

diff = year_2024 - now
print(diff)

diff = year_2024.date() - current_date
print(diff)

from datetime import timedelta

start_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=13)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)
