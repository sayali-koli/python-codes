def mutate(x):
    x[0] = 100
    x.append(200)
    print(f"inside function : {x}")


nums = [10, 20, 30, 40]
mutate(nums)
print(f"outside function : {nums}")
