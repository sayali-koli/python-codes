# with open("hello.txt", "r") as f:
#     line1 = f.readline()
#     line2 = f.readline()
#     print(line1.strip())
#     print(line2.strip())


with open("hello.txt", "r") as f:
    lines = f.readlines()
    print(lines)

for line in lines:
    print(line.strip())
