my_list = [i for i in range(1, 11)]
print(my_list)


my_list = [i for i in range(10, 0, -1)]
print(my_list)


my_list = [i**2 for i in range(1, 11)]
print(my_list)

my_list = [i / 2 for i in range(1, 11)]
print(my_list)


my_list = [i - 1 for i in range(1, 11)]
print(my_list)


my_list = [i for i in range(1, 21) if i % 2 == 0]
print(my_list)


my_list = [i for i in range(1, 21) if i % 2 == 0 and i % 5 == 0]
print(my_list)


def is_prime(num):
    factor = 0
    for i in range(1, num + 1):
        if num % i == 0:
            factor += 1
    if factor == 2:
        return True
    return False


my_list = [i for i in range(1, 101) if is_prime(i) == True]
print(my_list)
