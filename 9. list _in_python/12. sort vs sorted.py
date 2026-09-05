# sorted create a new list id does not have the same

# nums = [4, 7, 3, 8, 1, 1, 2, 10, 9, 6, 9, 1, 1, 1]

# new_list = sorted(nums)
# print(f"new_list={new_list}", id(new_list))
# print(f"nums={nums}", id(nums))


# sort does not create new list they change in the list directly

# nums = [4, 7, 3, 8, 1, 1, 2, 10, 9, 6, 9, 1, 1, 1]
# print(f"nums={nums}", id(nums))
# nums.sort()
# print(f"nums={nums}", id(nums))


# nums = [4, 7, 3, 8, 1, 1, 2, 10, 9, 6, 9, 1, 1, 1]
# print(f"nums={nums}", id(nums))
# nums.reverse()
# print(f"nums={nums}", id(nums))


nums = [4, 7, 3, 8, 1, 1, 2, 10, 9, 6, 9, 1, 1, 1]
# nums.index(7)
# print(nums.index(4))

print(nums.count(8))

nums.clear()
print(nums)
