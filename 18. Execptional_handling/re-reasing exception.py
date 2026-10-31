def check_age():
    try:
        age = int(input("enter age: "))
        if age < 0:
            print("age is cannot be negative")
        elif age > 150:
            print("age is cannot be reail")
        else:
            print("age is good")
    except ZeroDivisionError:
        print(f"Invaild Number")
    except ValueError as e:
        print(f"inside function error : {e}")
        raise
    except Exception as e:
        print(f"inside function error : {e}")


try:
    check_age()
except Exception as e:
    print(f"outside error:{e}")
else:
    print("success")
