old = open("old.txt", "r")
new = open("new.txt", "a")

new.write(old.read())
old.close()
new.close()

new = open("new.txt", "r")
print(new.read())