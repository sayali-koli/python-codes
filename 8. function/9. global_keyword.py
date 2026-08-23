count = 0


def increase():
    global count
    count = 2
    print(f"inside function count={count}")


increase()
print(f"outside function count={count}")
