import re

txt = input()
x = re.search(r"ab*$", txt)

if x:
    print("Match!")
else:
    print("Does not match!")