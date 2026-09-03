nums = [56, 34, 25, 40, 70, 77, 17, 59, 60, 66, 47]

for index, value in enumerate(nums):
    print(f"index={index} and value={value}")


for index, value in enumerate(nums):
    if value % 2 == 0:
        print(index)
