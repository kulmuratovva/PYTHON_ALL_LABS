import re

txt = input()
x = re.sub(r"[ .,]", ":", txt)
print(x)