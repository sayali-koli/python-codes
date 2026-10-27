# class vehical:
#     def __init__(self, brand):
#         self.brand = brand

#     def start(self):
#         print(f"{self.brand} starting up....")


# class car(vehical):
#     def drive(self):
#         print(f"{self.brand}driving...")


# v = car("maruti")
# v.drive()
# v.start()


class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} is specking....")

    def sleep(self):
        print(f"{self.name} is sleeping...")


class Dog(Animal):
    pass


d1 = Animal("gimmi", 5)
d1.speak()
d1.sleep()
