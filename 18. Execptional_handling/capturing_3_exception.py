try:
    num1 = int(input("enter no 1 : "))
    num2 = int(input("enter no 2 : "))
    print(f"num1/num2 : {num1/num2}")

except Exception as e:
    print(type(e).__name__)
    print(f"error message:{e}")

print("invilid ")
