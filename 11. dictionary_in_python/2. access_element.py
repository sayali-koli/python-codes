marks = {
    "science": 80,
    "maths": 90,
    "comp": 95,
    "hindi": 43,
    "history": 71,
    1: 100,
}

print(marks["science"])
print(marks[1])

# methods

print(marks.get("sciencee", 0))


subject = "history"
ans = marks.get(subject)
if ans is None:
    print("subject not found")
else:
    print(f"marks scored:{ans}")
