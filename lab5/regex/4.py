import re

txt = input()
x = re.search(r"^[A-Z][a-z]+$", txt)

if x:
    print("Match!")
else:
    print("Does not match!")