# def greet(name, age):
#     return f"your name is {name},and your age is {age} years"

#     print("gn")
#     print("morning")
#     print("done")


# print(greet("sayali", 22))


def is_prime(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False


print(is_prime(20))
