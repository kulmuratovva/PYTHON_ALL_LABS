import re

txt = input()
x = re.sub(r"[_]", "", txt)
print(x)