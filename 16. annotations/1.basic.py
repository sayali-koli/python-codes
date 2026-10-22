def calaculation(a: int, b: float) -> int:
    return a + b


def cal_maximum(a: int, b: int, c: int) -> None:
    print(f"maximum of a,b,c,is {max(a,b,c)}")


def greet(name: str, age: int, marks: float, adult: bool):
    return f"name is:{name}\nage is :{age}\nmarks is:{marks}\nadult is :{adult}"


print(calaculation(2, 4.6))
cal_maximum(2, 5, 9)
print(greet("sayali", 22, 12.4, True))
