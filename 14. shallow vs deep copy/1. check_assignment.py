orignal = [1, 2, 3]
copy = orignal

copy.append(100)

print(id(orignal))
print(id(copy))

print(orignal is copy)
print(orignal == copy)

print(orignal)
print(copy)


a = [4, 5, 6]
b = [4, 5, 6]
print(a is b)
print(a == b)
