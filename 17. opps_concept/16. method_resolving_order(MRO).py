class A:
    def hello(self):
        print("hello form A")


class B(A):
    def hello(self):
        print("hello form B")


class C(A):
    def hello(self):
        print("hello form C")


class D(B, C):
    def hello(self):
        print("hello form D")


d = C()
d.hello()
print(C.__mro__)
