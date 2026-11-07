def addition(a: int, b: int) -> int:
    return a + b


def substraction(a: int, b: int) -> int:
    return a - b


def multiplication(a: int, b: int) -> int:
    return a * b


def division(a: int, b: int) -> float:
    return a / b


pi = 3.14


if __name__ == "__main__":
    print(f"calculater file__name__:{__name__}")
    print(f"testing this code-START")
    result = addition(10, 20)
    print(f"addition answer = {result}")
    print("testing this code-END")
