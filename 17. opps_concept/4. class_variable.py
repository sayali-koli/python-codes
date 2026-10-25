class Student:
    school = "zeal egucation socity"

    def __init__(self, name: str):
        self.name = name


s1 = Student("sayali")
s2 = Student("suajl")

print(s1.name)  # instance variables
print(s2.name)  # instance variables
print(s1.school)
print(s2.school)
print(Student.school)

# 1st way to change the class variable

Student.school = "xyz"
print(Student.school)
print(s2.school)

# 2nd way to change the class variable (only for specific object/instance)

s1.school = "zeal"
print(s1.school)
