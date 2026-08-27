# def even_odd():
#     num = int(input("enter your number : "))
#     is_check = "even" if num % 2 == 0 else "odd"
#     print(is_check)


# even_odd()
# even_odd()
# even_odd()
# even_odd()
# even_odd()


# def factors():
#     num = int(input("enter your number : "))
#     for i in range(1, num + 1):
#         if num % i == 0:
#             print(i, end=" ")


# factors()


# def fizzbuzz(n):
#     if n % 3 == 0:
#         return "Fizz"
#     elif n % 5 == 0:
#         return "Buzz"
#     elif n % 3 == 0 and n % 5 == 0:
#         return "FizzBizz"
#     return n


# ans = fizzbuzz(15)
# print(ans)


# def power(base, exp):
#     if exp < 0:
#         base = 1 / base
#         exp = -exp

#     pw = 1
#     for i in range(exp):
#         pw = pw * base
#     return pw


# num1 = int(input("enter your base number : "))
# num2 = int(input("enter your exponent number : "))

# print(power(num1, num2))


def tax_calculation(income):
    if income <= 250000:
        tax = 0
    elif income > 250000 and income >= 5000000:
        tax = income * 0.05
    elif income > 500000 and income >= 1000000:
        tax = income * 0.20
    elif income < 1000000:
        tax = income * 0.30

    return tax


print(tax_calculation(1000000))
