# Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.

def isDivBy(a, b):
    return (i for i in range(a, b) if i % 3 == 0 and i % 4 == 0)

a = int(input())
b = int(input())

for i in isDivBy(a, b):
    print(i, end=" ")