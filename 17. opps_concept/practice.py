# class Movie:
#     def __init__(self, title: str, director: str, year: int, rating: int | float):
#         self.title = title
#         self.director = director
#         self.year = year
#         self.rating = rating

#     def is_class(self):
#         if 2026 - self.year >= 25:
#             return True
#         else:
#             return False


# s = Movie("sairat", "nagraj manjule", 2026, 4.5)
# print(s.is_class())


# class Employee:
#     def __init__(self, name: str, salary: int | float, department: str):
#         self.name = name
#         self.salary = salary
#         self.department = department

#     def give_raise(self, amount) -> int:
#         self.salary += amount

#     def display_detalis(self):
#         print(f"name={self.name}")
#         print(f"salary:{self.salary}")
#         print(f"department:{self.department}")


# e1 = Employee("sayali", 95000, "data scientist")
# e2 = Employee("sujal", 100000, "data anylist")
# e3 = Employee("anuj", 65000, "nda")

# e1.give_raise(500)


# e1.display_detalis()
# print("=" * 10)
# e2.display_detalis()
# print("=" * 10)
# e3.display_detalis()


# class Calculater:
#     def __init__(self, a: int, b: int):
#         self.a = a
#         self.b = b

#     def calculation(self):
#         self.addd = self.a + self.b
#         self.substract = self.a - self.b
#         self.multiplication = self.a * self.b
#         self.divide = self.a / self.b
#         return self.addd, self.substract, self.multiplication, self.divide

#     def display_details(self):
#         print(f"addd:{self.addd}")
#         print(f"substract:{self.substract}")
#         print(f"multiplication:{self.multiplication}")
#         print(f"divide:{self.divide}")


# a = Calculater(2, 10)
# a.calculation()
# a.display_details()


# class Book:
#     def __init__(self, title: str, author: str, pages: int):
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def display_details(self):
#         print(f"title:{self.title}\nauthor:{self.author}\npages:{self.pages}\n")


# b1 = Book("richdadpoordad", "santosh", 500)
# b2 = Book("sairat", "nagrajmangule", 900)
# b3 = Book("48 law of power", "sayali", 300)

# b1.display_details()
# b2.display_details()
# b3.display_details()


# import math


# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius * self.radius

#     def circumference(self):
#         return 2 * math.pi * self.radius,


# c1 = Circle(4)
# print(c1.area())
# print(c1.circumference())


# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def deposite(self, amount):
#         self.amount = amount
#         self.balance += amount
#         return self.balance

#     def withdraw(self, amount):
#         self.amount1 = amount
#         self.balance -= self.amount1
#         return self.balance


# b1 = BankAccount("sayali koli", 100000)
# print(b1.deposite(500))
# print(b1.withdraw(10000))
# print(f"owner name:{b1.owner}\nbalance:{b1.balance}")


# class Rectangle:
#     def __init__(self, width: int, height: int):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

#     def perimeter(self):
#         return (self.width + self.height) * 2

#     def is_square(self):
#         if self.width == self.height:
#             return True
#         return False


# r1 = Rectangle(2, 4)
# print(r1.area())
# print(r1.perimeter())
# print(r1.is_square())


# class StringUtils:

#     @staticmethod
#     def is_palindrome(s):
#         if s[0:] == s[::-1]:
#             return "palindrome"
#         return "not a palindrome"

#     @staticmethod
#     def reverse_string(s):
#         return s[::-1]


# print(StringUtils.is_palindrome("nitin"))
# print(StringUtils.reverse_string("sayali"))


# class Product:
#     tax_rate = 0.18

#     def __init__(self, name: str, price: int):
#         self.name = name
#         self.price = price

#     def final_price(self):
#         return self.price * (1 + Product.tax_rate)

#     @classmethod
#     def update_tax_rate(cls, new_tax: int):
#         cls.tax_rate = new_tax
#         print(f"tax rate updated to {cls.tax_rate*100:.2f}%")


# p1 = Product("santoor", 55)
# print(f"product : {p1.name}")
# print(f"price : {p1.price}")
# print(f"price+tax : {p1.final_price()}")
# Product.update_tax_rate(10.0)
# print(f"new final price:{p1.final_price()}")


# class Temperature:
#     def __init__(self, celsius):
#         self.__celsius = celsius

#     @property
#     def celsius(self):
#         return self.__celsius

#     @celsius.setter
#     def set_celsius(self, value):
#         if value > -273.15:
#             self.__celsius = value
#         else:
#             raise ValueError("enter valid number")


# t1 = Temperature(60)
# print(t1.celsius)
# t1.set_celsius = 77
# print(t1.set_celsius)


# class Shapes:

#     def discribe(self):
#         print("i am a shape")


# class Circle(Shapes):
#     def discribe(self):
#         print("i am a circle")


# s1 = Shapes()
# s2 = Circle()
# s1.discribe()
# s2.discribe()


# class Employee:
#     def __init__(self, name: str, salary: int):
#         self.name = name
#         self.salary = salary

#     def discription(self):
#         print(f"Employee name : {self.name}")
#         print(f"Employee salary : {self.salary}")


# class Manager(Employee):
#     def __init__(self, name: str, salary: int, teamsize: int):
#         super().__init__(name, salary)
#         self.teamsize = teamsize

#     def discription(self):
#         print(f"manager name : {self.name}")
#         print(f"salary : {self.salary}")
#         print(f"team size : {self.teamsize}")


# e1 = Employee("sayali", 100000)
# e2 = Manager("sujal", 50000, 5)

# e1.discription()
# e2.discription()


import math
class Shapes:
    list=[]

class Square(Shapes):
    def area(self,side:int):
        sqr=side*side 
        return Shapes.list.append(f"square : {sqr}")
       
class Rectangle(Shapes):
    def area(self,length:int,breadth:int):
        rect=length*breadth 
        return Shapes.list.append(f"Rectangle : {rect}")       
    
class Circle(Shapes):
    def area(radius:int):
        cir=math.pi*radius*radius
        return Shapes.list.append(f"circle : {cir}")   

    
