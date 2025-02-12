# Create a generator that generates the squares of numbers up to some number N.

n = int(input())

for i in (i**2 for i in range(1, n + 1)):
    print(i, end=" ")