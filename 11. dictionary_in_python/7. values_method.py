marks = {
    "science": 80,
    "maths": 90,
    "comp": 95,
    "hindi": 43,
    "history": 71,
}

print(marks.values())

total = 0
for mark in marks.values():
    total += mark
    print(mark)
print(f"total={total}")
