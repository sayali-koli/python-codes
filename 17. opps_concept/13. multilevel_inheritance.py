class Animal:
    def breathe(self):
        print("breathing...")


class Mammel(Animal):
    def feed_young(self):
        print("feeding young...")


class Dog(Animal):
    def bark(self):
        print("woof!")


d = Dog
d.breathe()
d.feed_young()
d.bark()
