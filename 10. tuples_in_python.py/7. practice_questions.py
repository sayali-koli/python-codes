# tuple = (
#     "mahi way",
#     "sairat",
#     "tarakmantra",
#     "pandurang",
#     "abhanga",
#     "kal ho na ho",
# )
# n = len(tuple)
# # print(tuple[0])
# # print(tuple[n // 2])
# # print(tuple[-1])
# print(
#     f"my first song={tuple[0]} and second song={tuple[n//2]}and third song={tuple[-1]}"


# tuple = (1, 2, 3, 4, 5, 6, 7, 8)
# print(tuple[0:3])
# print(tuple[-1:-4:-1])
# print(tuple[0:8:2])
# print(
#     f"first three element={tuple[0:3]}\nlast three element={tuple[-1:-4:-1]}\nalternate element={tuple[0:8:2]}")


# marks = 50, 40, 80, 90, 95, 99
# total = sum(marks)
# n = len(marks)
# maxi = max(marks)
# mini = min(marks)

# average = total / 6
# print(total)
# print(average)
# print(mini, maxi)

# print(
#     f"highest marks of student is={maxi}\nlowest marks of student is={mini}\nthe total is={total}\nthe average is={average:.2f}")


# num1 = int(input("enter your number : "))
# num2 = int(input("enter your number : "))
# num3 = int(input("enter your number : "))
# num4 = int(input("enter your number : "))
# num5 = int(input("enter your number : "))

# my_tuple = num1, num2, num3, num4, num5
# maxi = max(my_tuple)
# mini = min(my_tuple)
# print(maxi, mini)
# print(f"maximum number={maxi}\nminimum number={mini}")


# num1, num2, num3 = map(int, input("enter your number : ").split())
# print(num1, num2, num3)


def get_stats(nums):
    n = len(nums)
    total = sum(nums)
    average = total / n
    maxi = max(nums)
    mini = min(nums)
    return (total, average, mini, maxi)


my_tuple = 1, 2, 3, 4, 56, 80
total, average, min, max = get_stats(my_tuple)
print(f"total= {total}")
print(f"average= {average}")
print(f"maximum={max}")
print(f"minimum= {min}")
