class Student:
    def __init__(self, name: str, age: int, roll_no: int, gender: str):
        self.name = name
        self.age = age
        self.roll_no = roll_no
        self.gender = gender

    def display_details(self):
        print(f"name:{self.name}")
        print(f"age:{self.age}")
        print(f"roll_no:{self.roll_no}")
        print(f"gender:{self.gender}")


student1 = Student("sayali", 22, 1, "female")
student1.display_details()
