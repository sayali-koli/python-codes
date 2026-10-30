# try:
#     num1 = int(input("enter no 1 : "))
#     num2 = int(input("enter no 2 : "))
#     print(f"num1/num2 : {num1/num2}")
# except ZeroDivisionError:
#     print("cannort divide by zero,enter proper integer")
# except ValueError:
#     print("enter proper integer")


try:
    num = int(input("enter a number :"))
    result = 100 / num
    print(f"{result:.2f}")

except (ValueError, ZeroDivisionError):
    print("cannot divide by zero,invalid input try again")
