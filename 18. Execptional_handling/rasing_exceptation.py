def check_age(age: int):
    if age < 0:
        raise ValueError("age is cannot be negative")
    elif age > 150:
        raise ValueError("age is cannot be reail")
    print("age is good")


try:
    check_age(0)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)
