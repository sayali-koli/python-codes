class Student:
    def __init__(self, name: str, age: int, marks: list[int]):
        self.name: str = name
        self.age: int = age
        self.marks: list[int] = marks

    def total(self):
        return sum(self.marks)

    def average(self):
        return sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.average()

        if avg >= 90:
            return "A"
        elif avg >= 50 and avg <= 80:
            return "B"
        else:
            return "c"


student1 = Student("sayali", 22, [10, 20, 30, 40])
total = student1.total()
average = student1.average()
print(f"total:{total}\naverage:{average}\ngrade:{student1.grade()}")
