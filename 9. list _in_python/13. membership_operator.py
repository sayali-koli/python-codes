nums = [4, 7, 3, 8, 1, 1, 2, 10, 9, 6, 9, 1, 1, 1]
# print(91 in nums)
# print(4 in nums)
# print(100 in nums or 3 in nums)


target = int(input("ENter Target = "))

if target in nums:
    nums.remove(target)
    print(f"nums = {nums}")
else:
    print("Cannot remove the target, target does not exist")
