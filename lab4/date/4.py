# Write a Python program to calculate two date difference in seconds.

import datetime

x = datetime.datetime.now()
y = datetime.datetime.now() - datetime.timedelta(10)

print(y.strftime("%S"))