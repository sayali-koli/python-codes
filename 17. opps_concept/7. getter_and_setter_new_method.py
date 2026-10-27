class Student:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def set_name(self, new_name):
        if new_name != "":
            self.__name = new_name


s1 = Student("sayali")
print(s1.name)
s1.set_name = "shubhnqgi"
print(s1.name)
