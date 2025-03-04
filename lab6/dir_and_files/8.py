import os

path = input()

if os.access(path, os.F_OK) and os.access(path, os.W_OK):
    print("File exists and can be deleted.")
    os.remove(path)
    
else:
    print("The file does not exist or cannot be deleted.")