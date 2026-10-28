class Animal:
    def __init__(self, name):
        self.name = name

    def breadthe(self):
        print(f"{self.name} is breadthing")


class Dog(Animal):
    def bark(self):
        print("Woof!")


class cat(Animal):
    def meow(self):
        print("Meow!")


class cow(Animal):
    def moo(self):
        print("Moo!")


d = Dog("tommy")
c = cat("sonu")
cow = cow("bssie")
d.breadthe()
c.breadthe()
cow.breadthe()
