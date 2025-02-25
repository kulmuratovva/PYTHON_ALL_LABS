import re

txt = input()
x = re.search(r"[a-z]+(?:_[a-z]+)+$", txt)

if x:
    print("Match!")
else:
    print("Does not match!")