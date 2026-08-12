"""
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
"""

for i in range(1, 6):
    for k in range(1, 6 - i):
        print(" ", end=" ")
    for j in range(1, i * 2):
        print("*", end=" ")
    print()

for i in range(4, 0, -1):
    for k in range(1, 5 - i + 1):
        print(" ", end=" ")
    for j in range(1, i * 2):
        print("*", end=" ")
    print()


for i in range(1, 5):
    for j in range(1, 9):
        if i == 1 or i == 4 or j == 1 or j == 8:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
