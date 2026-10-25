class Student:
    def __init__(self, name):
        self.__name = name

    # getter
    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name


s1 = Student("sayali")
print(s1.get_name())
s1.set_name("shubhangi")
print(s1.get_name())
