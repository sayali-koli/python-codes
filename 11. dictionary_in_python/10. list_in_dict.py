student = {
    "name": "Rahul",
    "age": 21,
    "subjects": ["Math", "Science", "English"],
    "marks": [85, 92, 78],
}

# print(student["name"])
# print(student["subjects"][0])
# print(student["marks"][0])
# print(student["subjects"][2])


# print(sum(student["marks"]))

for key, details in student.items():
    print(f"subject : {details['subject']} and marks : {details['marks']}")
