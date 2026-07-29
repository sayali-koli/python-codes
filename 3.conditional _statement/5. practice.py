# num = int(input("enter your number : "))
# if num > 0:
#     print("positive")
# elif num < 0:
#     print("negative")
# else:
#     print("zero")

# num1 = int(input("enter your number : "))
# num2 = int(input("enter your number : "))

# if num1 > num2:
#     print("num1 is grater number")
# elif num1 < num2:
#     print("num2 is grater number")
# elif num1 == num2:
#     print("both are equal")

# year = int(input("enter your year : "))

# if (year % 4==0 and year %100 !=0) and (year % 400==0):
#     print("leap year")
# else:
#     print("not a leap year")


# a = int(input("enter your number1 : "))
# b = int(input("enter your number2 : "))
# c = int(input("enter your number3 : "))

# if a > b and a > c:
#     print("a is the largest number")
# elif b > a and b > c:
#     print("b is the largest number")
# else:
#     print("c is the largest number")


# age = int(input("enter your age : "))
# valid_id = input("do you have valid_id : ")

# if age >=18:
#     if valid_id=="yes":
#         print("you can enter the venue")
#     else:
#         print("cannot enter in vanue because you not have valid_id ")
# else:
#     print("you are not allowed in the venue becouse you age is less than 18")


# num = int(input("enter your number : "))
# status = "even" if num % 2 == 0 else "odd"
# print(f"the number is {status}")


# discount = int(input("enter your discount : "))

# if discount > 5000:
#     prize = discount * 0.20
# elif discount > 2000:
#     prize = discount * 0.10
# elif discount > 1000:
#     prize = discount * 0.05
# else:
#     "no discount"

# final_amount = discount - prize

# print(f"the discount is applied on amont, you have to pay {final_amount}")

amount = float(input("Enter purchase amount: "))

if amount > 5000:
    discount = amount * 0.20
elif amount > 2000:
    discount = amount * 0.10
elif amount > 1000:
    discount = amount * 0.05
else:
    discount = 0

final_amount = amount - discount

print("Discount:", discount)
print("Final Amount:", final_amount)
