num = [56, 34, 25, 40, 70, 77, 17, 59, 60, 66, 47]
n = len(num)
count = 0
i = 0
while i <= n - 1:
    if num[i] % 2 == 0:
        count += 1
    i += 1
print(count)


num = [56, 34, 25, 40, 70, 77, 17, 59, 60, 66, 47]
i = n - 1
while i >= 0:
    print(num[i])
    i -= 1
