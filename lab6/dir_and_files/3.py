import os

path = input("Enter the path: ")

if os.access(path, os.F_OK):
    print("File exists")

    print("Direction name: ", os.path.dirname(path))
    print("File name: ", os.path.basename(path))
else:
    print("File does not exist")
