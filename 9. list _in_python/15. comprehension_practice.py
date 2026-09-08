my_list = [i * i for i in range(1, 21) if i % 2 != 0]
print(my_list)


marks = [65, 80, 70, 90, 75, 82, 60]
new_marks_list = [nums for nums in marks if nums >= 75]
print(new_marks_list)
