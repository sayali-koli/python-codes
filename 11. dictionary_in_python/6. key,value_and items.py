marks = {
    "science": 80,
    "maths": 90,
    "comp": 95,
    "hindi": 43,
    "history": 71,
}


print(marks.keys())

total = 0
for sub in marks:
    # print(sub, marks[sub])
    total += marks[sub]
    print(f"subject={sub} and marks={marks[sub]}")
print(f"total={total}")
