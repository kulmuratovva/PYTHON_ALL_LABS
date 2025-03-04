import os

path = input("Enter the path to your file: ")

if os.access(path, os.F_OK):
    print("File exists")

    print("readability: ", os.access(path, os.R_OK))
    print("writability: ", os.access(path, os.W_OK))
    print("executability: ", os.access(path, os.X_OK))
else:
    print("File does not exist")