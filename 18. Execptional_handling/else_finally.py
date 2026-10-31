try:
    num = int(input("enter a number :"))
    result = 100 / num
except ValueError:
    print("that is not valid number")
except ZeroDivisionError:
    print("you cannot divide by zero")
else:
    print(f"result:{result:.2f}")
finally:
    print("calculation attempt is completed")
