import re

txt = input()
x = re.search(r"^ab{2,3}$", txt)

if x:
    print("Match!")
else:
    print("Does not match!")