# class Students:
#     # attributs
#     name = ""
#     age = "0"
#     gender = ""
#     roll_no = "0"


# student1 = Students()
# student2 = Students()
# student1.name = "sayali"
# student1.age = "23"
# student1.gender = "femal"
# student1.roll_no = 1
# print(student1)
# print(student1.name)
# print(student1.age)
# print(student1.gender)
# print(student1.roll_no)

# print("===============")

# print(student2)
# print(student2.name)
# print(student2.age)
# print(student2.gender)
# print(student2.roll_no)


class Students:
    # attributs
    name = ""
    age = "0"
    gender = ""
    roll_no = "0"

    # def set_details(self):
    #     self.name = input("enter name : ")
    #     self.age = int(input("enter your age : "))
    #     self.gender = input("enter gender : ")
    #     self.roll_no = input("enter roll_no : ")

    def set_details(self, n: str, a: int, g: str, r: int):
        self.name = n
        self.age = a
        self.gender = g
        self.roll_no = r

    def display_details(self) -> None:
        print(f"name={self.name}")
        print(f"age :{self.age}")
        print(f"gender :{self.gender}")
        print(f"roll_no :{self.roll_no}")


student1 = Students()
student2 = Students()
student1.set_details("sayali", 22, "femal", 1)
student2.set_details("sujal", 23, "male", 2)
student2.display_details()
