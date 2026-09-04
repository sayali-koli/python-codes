# numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# maxi = float("-inf")
# for num in numbers:
#     if num > maxi:
#         maxi = num
# print(f"largest number:{maxi}")


# numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# maxi = float("inf")
# for num in numbers:
#     if num < maxi:
#         maxi = num
# print(f"largest number:{maxi}")


# def does_target_exist(list, target):
#     for num in my_list:
#         if num == target:
#             return "exist in the list"
#     return "does not exist in the list"


# my_list = [10, 20, 30, 40, 50]

# print(does_target_exist(my_list, 30))
# print(does_target_exist(my_list, 60))


# nums = [85, 90, 78, 92, 88]
# n = len(nums)
# total = 0
# for num in nums:
#     total = total + num
# average = total / n
# print(total)
# print(n)
# print(average)


# def avg(lst):
#     n = len(scores)
#     total = 0
#     for num in scores:
#         total += num

#     average = total / n
#     return average


# scores = [85, 90, 78, 92, 88]
# print(avg(scores))


# def add_two_list(lst1, lst2):
#     new_list = []
#     n = len(lst1)
#     for i in range(0, n):
#         total = lst1[i] + lst2[i]
#         new_list.append(total)
#     return new_list


# list1 = [10, 20, 30, 40, 50]
# list2 = [1, 2, 3, 4, 5]

# print(add_two_list(list1, list2))


# def is_sorted(lst):
#     n = len(lst)
#     for i in range(0, n - 1):
#         if lst[i] > lst[i + 1]:
#             return False
#     return True


# numbers = [1, 20, 10, 15, 20, 25, 30]
# print(is_sorted(numbers))


# def largest_smallest(lst):
#     n = len(lst)
#     maxi1 = float("-inf")
#     maxi2 = float("inf")

#     for num in lst:
#         if num > maxi1:
#             maxi1 = num

#     for num in lst:
#         if num < maxi2:
#             maxi2 = num

#     return f"largest is {maxi1} smallest is {maxi2}"


# my_list = [3, 1, 4, 1, 5]
# print(largest_smallest(my_list))


# def reverse_list(lst):
#     n = len(lst)
#     new_list = []
#     for i in range(n - 1, -1, -1):
#         new_list.append(lst[i])
#     return new_list


# my_list = [1, 2, 8, 4, 5]
# print(reverse_list(my_list))


# def add_list(lst1, lst2):

#     new_list = lst1 + lst2
#     return new_list


# list1 = [1, 2]
# list2 = [3, 4]
# print(add_list(list1, list2))


# def add_list(lst1, lst2):
#     n = len(lst1)
#     new_list = []
#     for i in range(0, n):
#         add = lst1[i] + lst2[i]
#         new_list.append(add)
#     return new_list


# list1 = [1, 2]
# list2 = [3, 4]
# print(add_list(list1, list2))


# def add_list(lst1, lst2):
#     new_list = []
#     for nums in lst1:
#         new_list.append(nums)
#     for nums in lst2:
#         new_list.append(nums)

#     return new_list


# list1 = [1, 2]
# list2 = [3, 4]
# print(add_list(list1, list2))


# def remove_dublicates(lst):
#     result = []
#     for nums in lst:
#         if nums not in result:
#             result.append(nums)
#     return result


# nums = [1, 1, 2, 3, 4, 5, 5, 6, 6, 7, 7, 8, 9, 9, 0, 10]

# print(remove_dublicates(nums))


# def even_odd(lst):
#     even = []
#     odd = []
#     for num in lst:
#         if num % 2 == 0:
#             even.append(num)
#         else:
#             odd.append(num)
#     return even, odd


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(even_odd(numbers))


# def square_num(lst):
#     square = []
#     for nums in lst:
#         sqa = nums**2
#         square.append(sqa)
#     return square


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(square_num(numbers))


# def remove_dublicate(lst, target):
#     new_list = []

#     for nums in lst:
#         if nums != target:
#             new_list.append(nums)
#     return new_list


# n = int(input("enter your number : "))
# my_list = [10, 20, 10, 30, 20, 10, 40]
# print(remove_dublicate(my_list, n))


def replace_negative(lst):
    n = len(lst)
    for i in range(0, n):
        if lst[i] < 0:
            lst[i] = 0
    return lst


numbers = [5, -3, 8, -1, 7, -10, 12]
print(replace_negative(numbers))
