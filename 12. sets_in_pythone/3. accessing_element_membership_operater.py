fruits = {"apple", "mango", "banana"}
print("apple" in fruits)
print("tomato" in fruits)
print("kevi" not in fruits)


allowed_user = {"sayali", "sujal", "manish"}

user = input("enter your user : ")
if user in allowed_user:
    print("this is allowed,valid")
else:
    print("this is not allowed, not valid")
