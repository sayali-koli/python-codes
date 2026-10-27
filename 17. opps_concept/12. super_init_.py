class vehical:
    def __init__(self, brand: str):
        print("this is a vehical constructor")
        self.brand = brand


class car(vehical):
    def __init__(self, fuel: str, brand: str):
        print("this is a car constructor")
        super().__init__
        self.fuel = fuel

    def display(self):
        print(f"you have a {self.brand} car with{self.fuel} type")


car = car("petrol", "maruti")
car.display()
