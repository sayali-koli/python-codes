# square for 1 t0 10 using dict comprehension

# square = {i: i**2 for i in range(1, 11)}
# print(square)


# marks = {"math": 85, "science": 92, "english": 60, "hindi": 45}

# top = {sub: m for sub, m in marks.items() if m > 80}
# print(top)


# marks = {"math": 85, "science": 92, "english": 60, "hindi": 45}
# top = {sub: m * 2 for sub, m in marks.items()}
# print(top)


# zip()"create a dict form two lists"

subject = ["math", "science", "english"]
score = [85, 92, 78]

result = {sub: scr * 2 for sub, scr in zip(subject, score)}
print(result)
