# Write a Python program to write a list to a file.
list = [
    "5. Write a Python program to write a list to a file.", 
    "6. Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt."
]
f = open("c.txt", "a")

f.write("\n")
for i in list:
    f.write(i + "\n")

f.close()

f = open("c.txt", "r")
print(f.read())
f.close()