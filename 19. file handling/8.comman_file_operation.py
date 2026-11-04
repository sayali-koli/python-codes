import os
from pathlib import Path

# os.mkdir("my_folder")
# Path("my_folder1").mkdir()

# os.remove("new.txt")
# Path("new.txt").unlink()

# os.rename("hello.txt","hello_new.txt")
# Path("hello_new.txt").rename("hello.txt")


# for f in os.listdir("."):
#     print(f)

for f in Path("C://").iterdir():
    print(f)
