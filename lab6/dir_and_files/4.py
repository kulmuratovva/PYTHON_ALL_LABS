f = open("c.txt", "r")
cnt = sum(1 for line in f)
print(cnt)
f.close()