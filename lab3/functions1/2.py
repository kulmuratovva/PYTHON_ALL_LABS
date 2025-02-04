def celsius(f):
    c = (5 / 9) * (f - 32)
    return c

f = float(input("Fahrenheit: "))
c = celsius(f)
print(f"{c:.2f} celsius")