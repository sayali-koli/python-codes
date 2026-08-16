# def add(a, b):
#     sum = a + b
#     print(f"total={sum}")


# num1 = int(input("enter your number : "))
# num2 = int(input("enter your number : "))
# add(num1, num2)


# def rectengle_area(length, breath):
#     area = length * breath
#     print(area)


# rectengle_area(10, 2)


# def find_max(a, b, c):
#     if a > b and a > c:
#         print("a is the largest")
#     elif b > a and b > c:
#         print("b is the largest")
#     else:
#         print("c is the largest")


# num1 = int(input("enter your number : "))
# num2 = int(input("enter your number : "))
# num3 = int(input("enter your number : "))
# find_max(num1, num2, num3)


def discount_price(original_price, discount_percent):
    discount_price = original_price * (discount_percent / 100)
    final_amount = original_price - discount_price
    print(f"your total amount={final_amount}")


discount_price(6000, 31)
