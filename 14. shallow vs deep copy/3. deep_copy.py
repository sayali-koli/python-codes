import copy

orignal = [1, 23, 4, 5, 6, [23, 45, 6, 778], 99, 200]
shallow = copy.deepcopy(orignal)

print(id(orignal))
print(id(shallow))

shallow[5][2] = 999
shallow[7] = 300

print(orignal)
print(shallow)
