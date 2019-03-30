a = [11, 22, 11]
b = set(a)
c = set([11, 22, 33, 44])

for i in b:
    print(i)

print(c-b)