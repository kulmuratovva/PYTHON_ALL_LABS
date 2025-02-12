# Write a Python program to calculate the area of regular polygon.
import math

n = 4
l = 25

area = (n * l**2) / (4 * math.tan(math.pi / n))

print(int(area))