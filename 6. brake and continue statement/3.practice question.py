# total = 0
# while True:
#     num = int(input("enter your number : "))
#     if num == 0:
#         break
#     if num < 0:
#         continue
#     total += num
# print(total)


# total = 0
# for i in range(20**20):
#     num = int(input("enter your number : "))
#     if num == 0:
#         break
#     if num < 0:
#         continue
#     total += num
# print(total)


total = 0
n = int(input("hoe many number do u want to enter ? : "))

for i in range(n):
    num = int(input("enter your number : "))
    if num == 0:
        break
    if num < 0:
        continue
    total += num
print(total)
