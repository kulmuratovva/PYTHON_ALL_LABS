import os

path = "."
items = os.listdir(path)

print("Directories:\n", [d for d in items if os.path.isdir(os.path.join(path, d))])
print()
print("Files:\n", [f for f in items if os.path.isfile(os.path.join(path, f))])