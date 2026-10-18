text = "sayalikoli"
print(text.isalpha())
print(text.isdigit())
print(text.isalnum())
print(text.isspace())
print(text.startswith("a"))
print(text.endswith("i"))


age = input("enter your age : ")
if age.isdigit():
    if int(age) >= 18:
        print("you can vote")
    else:
        print("you can not vote")
else:
    print("plz enter proper  age")
