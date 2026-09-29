students = {
    "101": {"name": "Rahul", "age": 21, "city": "Delhi"},
    "102": {"name": "Priya", "age": 20, "city": "Mumbai"},
    "103": {
        "name": "Karan",
        "age": 22,
        "city": "Pune",
        "details": {"phone": 8308259016, "gender": "female"},
    },
}

# how to access the data from dict in dict

# print(students["101"])
# print(students["101"]["name"])
# print(students["103"]["city"])
# print(students["103"]["details"]["gender"])

# iteration
total = 0
for roll_number, details in students.items():
    # print(f"roll_numbers : {roll_number} and details : {details}")
    total += details["age"]
    print(
        f"roll_number : {roll_number} , name :{details['name']} and age : {details['age']}"
    )
print(total)
