marks = [10, 20, 30, 40, 50]
n = len(marks)
print(f"length of list:{n}")

m = max(marks)
print(f"maximum marks is:{m}")

m = min(marks)
print(f"minimum marks is: {m}")

s = sum(marks)
print(f"sum of the marks:{s}")

new_list = sorted(marks)
print(f"new_list:{new_list}")


new_list = sorted(marks, reverse=True)
print(f"new_list:{new_list}")
