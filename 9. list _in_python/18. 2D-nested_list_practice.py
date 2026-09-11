# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]
# total = 0
# for i in range(0, 3):
#     for j in range(0, 3):
#         total = total + matrix[i][j]
#         # print(matrix[i][j],end=" ")
# print(total)


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]

# for i in range(0, 3):
#     for j in range(0, 3):
#         if matrix[0][1]:
#             for nums in matrix:
#                 matrix[0][1] = "*"
#         if matrix[0][2]:
#             for nums in matrix:
#                 matrix[0][2] = "*"
#         if matrix[1][2]:
#             for nums in matrix:
#                 matrix[1][2] = "*"

#         print(matrix[i][j], end=" ")
#     print()


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]

# for i in range(0, 3):
#     for j in range(0, 3):
#         if matrix[1][0]:
#             for nums in matrix:
#                 matrix[1][0] = "*"

#         if matrix[2][0]:
#             for nums in matrix:
#                 matrix[2][0] = "*"

#         if matrix[2][1]:
#             for nums in matrix:
#                 matrix[2][1] = "*"

#         print(matrix[i][j], end=" ")
#     print()


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
for i in range(0, 3):
    for j in range(0, 3):
        if matrix[0][1]:
            for nums in matrix:
                matrix[0][1] = "*"
        if matrix[0][2]:
            for nums in matrix:
                matrix[0][2] = "*"
        if matrix[1][2]:
            for nums in matrix:
                matrix[1][2] = "*"

        if matrix[1][0]:
            for nums in matrix:
                matrix[1][0] = "*"
        if matrix[2][0]:
            for nums in matrix:
                matrix[2][0] = "*"
        if matrix[2][1]:
            for nums in matrix:
                matrix[2][1] = "*"

        print(matrix[i][j], end=" ")
    print()
