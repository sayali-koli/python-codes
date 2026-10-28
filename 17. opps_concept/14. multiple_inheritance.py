class Flyer:
    def fly(self):
        print("flying")


class Swimmer:
    def swim(self):
        print("swimming")


class Duck(Flyer, Swimmer):
    def quack(self):
        print("Quack")


d = Duck()
d.quack()
d.fly()
d.swim()
