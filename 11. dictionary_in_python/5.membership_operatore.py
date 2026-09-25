student = {
    "name": "sayali",
    "age": 23,
    "gender": "femal",
    "city": "solapur",
    "father name": "jagdish koli",
    "phone no": 8308259016,
}

# print("age" in student)
# print(22 in student)


k = input("enter key : ")

if k in student:
    print(student[k])
else:
    print("key does not exist")
