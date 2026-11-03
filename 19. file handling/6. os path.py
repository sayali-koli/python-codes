import os

print(os.path.exists("hello.txt"))

print(os.path.isfile("hello.txt"))

print(os.path.isdir("hello.txt"))

print(os.path.getsize("hello.txt"))


path = os.path.join("folder", "log folder", "app.log")
print(path)
