marks = {
    "science": 80,
    "maths": 90,
    "comp": 95,
    "hindi": 43,
    "history": 71,
}

print(marks.items())

# for details in marks.items():
# print(details[0], details[1])


for details in marks.items():
    sub = details[0]
    marks = details[1]
    print(sub, marks)
