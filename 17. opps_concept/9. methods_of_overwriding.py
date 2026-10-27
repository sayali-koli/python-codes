class Animal:
    def speak(self):
        print("Animal is specking")


class Dog(Animal):
    def speak(self):
        print("Dog is barking")


d = Dog()
d.speak()
