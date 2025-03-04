txt = input()

cnt_upp = sum(1 for char in txt if char.isupper())
cnt_low = sum(1 for char in txt if char.islower())

print(f"There're {cnt_upp} uppercase, {cnt_low} lowercase letters")