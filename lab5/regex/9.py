import re

txt = input()
x = re.findall(r"[A-Z][^A-Z]*", txt)

res = " ".join(x)  # Объединяем слова через пробел
print(res)