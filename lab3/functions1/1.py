def ounce(gram):
    ounces = gram * 0.03527396
    return ounces

gram = float(input("Enter gram: "))
ounces = ounce(gram)

print(f"{ounces:.2f} ounces")