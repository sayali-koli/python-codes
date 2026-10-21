def rebinding(x):
    x = [1, 2, 3, 4, 5]
    print(f"inside function : {x}")


nums = [10, 20, 30, 40]
rebinding(nums)
print(f"outside function : {nums}")
