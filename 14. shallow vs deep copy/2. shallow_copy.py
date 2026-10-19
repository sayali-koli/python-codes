import copy

orignal = [1, 2, 3]
shallow = copy.copy(orignal)
# shallow=orignal.copy()
print(id(orignal))
print(id(shallow))

shallow.append(100)
# orignal.append(101)

print(orignal)
print(shallow)
