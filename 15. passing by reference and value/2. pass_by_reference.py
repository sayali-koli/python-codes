# def add_item(x):
#     x.append(100)
#     print(f"inside function : {x}")


# num = [1, 2, 3]
# add_item(num)
# print(f"outside function : {num}")


import copy


def add_item(x):
    x = copy.deepcopy(x)
    x.append(100)
    print(f"inside function : {x}")


num = [1, 2, 3]
add_item(num)
print(f"outside function : {num}")
