# student = {
#     "name": "sayali",
#     "city": "solapur",
#     "marks": [10, 20, 30, 40, 50],
# }

# print(f"name: {student["name"]}\ncity : {student["city"]}\nmarks : {student["marks"]}")


# marks = {
#     "science": 80,
#     "maths": 90,
#     "comp": 95,
#     "hindi": 43,
#     "history": 71,
# }

# sub = input("enter sub: ")
# ans = marks.get(sub, "not available")
# print(ans)


# product = {
#     "sope": 10,
#     "shampoo": 20,
#     "bottle": 100,
#     "bag": 500,
#     "phone": 15000,
# }

# sub = input("enter product : ")
# ans = product.get(sub)
# if ans is None:
#     print("product not found")
# else:
#     print(f"product = {sub}\nand price = {ans}")


# mapping = {
#     "india": "delhi",
#     "china": "bejing",
#     "germany": "Berlin",
#     "england": "londan",
#     "treland": "dublin",
# }

# for details in mapping.items():
#     x = details[0]
#     y = details[1]
#     print(x, y)


# marks = {
#     "science": 80,
#     "maths": 90,
#     "comp": 95,
#     "hindi": 43,
#     "history": 71,
# }
# total = 0
# n = len(marks)
# for mark in marks.values():
#     total += mark
#     average = total / n
# print(f"the total marks : {total} and average : {average}")


# # another way to sum or total
# total=sum(marks.values())


# student = {
#     "sayali": 50,
#     "sujal": 80,
#     "manish": 60,
#     "anuj": 90,
#     "zaid": 43,
# }

# for stud, mark in student.items():
#     if mark < 75:
#         print(f"student : {stud} and mark : {mark}")


# def marge_dicts(d1, d2):
#     new_dict = {}
#     new_dict.update(d1)
#     new_dict.update(d2)
#     print(new_dict)


# marks = {
#     "science": 80,
#     "maths": 90,
#     "comp": 95,
# }
# student = {
#     "sayali": 50,
#     "sujal": 80,
#     "manish": 60,
# }

# marge_dicts(marks, student)


# marks = {"science": 80, "maths": 90, "comp": 95, "hindi": 43, "history": 71, "geo": 99}

# highest = max(marks.items(), key=lambda x: x[1])
# lowest = min(marks.items(), key=lambda x: x[1])

# print(f"highest marks: {highest}and lowest: {lowest}")


# students = {
#     1: {"name": "Sujal", "age": 21, "city": "Pune"},
#     2: {"name": "Rahul", "age": 22, "city": "Mumbai"},
#     3: {"name": "Priya", "age": 20, "city": "Nashik"},
#     4: {"name": "Amit", "age": 23, "city": "Nagpur"},
# }

# for entry, details in students.items():
# print(f"student {entry}")
# print(f"name : {details["name"]}")
# print(f"age : {details["age"]}")
# print(f"city : {details["city"]}")
# print("=" * 30)
# print(f"entry:{entry} details:{details}")


# students = {
#     "sayali": [90, 80, 70],
#     "sujal": [40, 99, 70],
#     "manish": [30, 50, 60],
#     "anuj": [95, 89, 90],
#     "zaid": [66, 40, 20],
# }

# for student, marks in students.items():
#     n = len(students)
#     total = sum(marks)
#     average = total / len(marks)
# print(f"the total marks:{student} and\naverage marks is:{average}")
# print(f"student {student}")
# print(f"total marks : {total}")
# print(f"average : {average}")
# print("=" * 30)
# print(f"{student}has scored total marks{total} and his average is{average}")


# marks = {
#     "science": 80,
#     "maths": 90,
#     "comp": 95,
#     "hindi": 43,
#     "history": 71,
#     "geo": 99,
# }

# ans = sorted(marks.items(), key=lambda x: x[1], reverse=True)
# result = ans[0:3]
# # print(ans[0], ans[1], ans[2])

# for sub, mark in result:
#     print(f"subject : {sub}")
#     print(f"marks : {mark}")
#     print("=" * 2)


# cube = {i: i**3 for i in range(1, 11)}
# print(cube)


# marks = {
#     "science": 80,
#     "maths": 35,
#     "comp": 95,
#     "hindi": 30,
#     "history": 71,
#     "geo": 19,
# }

# new_dict = {sub: mark for sub, mark in marks.items()  if mark > 40}
# print(new_dict)


# subject = ["math", "science", "english"]
# score = [85, 92, 78]

# ans = {sub: scr for sub, scr in zip(subject, score)}
# print(ans)
