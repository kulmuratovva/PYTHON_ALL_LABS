import re

txt = input()
x = re.findall(r"[A-Z][^A-Z]*", txt)

print(x)