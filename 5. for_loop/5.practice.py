# sum = 0
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         sum = sum + i
# print("sum=", sum)


# num = int(input("enter your number : "))
# end = int(input("enter your end : "))
# for i in range(1, end + 1):
#     print(num * i)


# num = int(input("enter your number :"))
# for i in range(1, 11):
#     if num % 2 == 0:
#         print(num * i)


# num = int(input("enter your number :"))
# fact = 1
# for i in range(1, num + 1):
#     fact = fact * i
# print("factorial=", fact)


num = int(input("enter your number :"))
for i in range(1, 11):
    if num % i == 0:
        print(i)
