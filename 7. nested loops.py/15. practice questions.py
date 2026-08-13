"""
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15

"""

# num = 1
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(num, end=" ")
#         num += 1
#     print()


"""
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""

# for i in range(1, 6):
#     for j in range(1, 6):
#         print(j, end=" ")
#     print()


"""
* * * * *
*       *
*       *
*       * 
* * * * *
"""

# for i in range(1, 6):
#     for j in range(1, 6):
#         if i == 1 or i == 5 or j == 1 or j == 5:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


"""
*
* *
*   * 
*     * 
* * * * *
"""

# for i in range(1, 6):
#     for j in range(1, i + 1):
#         if i == 5 or j == 1 or j == i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


"""
1 0 1 0 1 
0 1 0 1 0
1 0 1 0 1
0 1 0 1 0
1 0 1 0 1
"""

# for i in range(1, 6):
#     for j in range(1, 6):
#         if (i + j) % 2 == 0:
#             print(1, end=" ")
#         else:
#             print(0, end=" ")

#     print()
