try:
    with open("hello.txt", "r") as f:
        for line in f:
            print(line.strip())
except FileExistsError:
    print("file does not find")
except:
    print("some error occure")
