start = int(input("enter your number : "))
end = int(input("enter your number : "))

i = start
while i <= end:
    if i % 3 == 0 and i % 4 == 0:
        print(i)
    i += 1
