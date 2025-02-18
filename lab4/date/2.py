# Write a Python program to print yesterday, today, tomorrow.

import datetime

now = datetime.datetime.now()
yesterday = datetime.datetime.now() - datetime.timedelta(1)
tomorrow = datetime.datetime.now() + datetime.timedelta(1)

print(now)
print(yesterday)
print(tomorrow)