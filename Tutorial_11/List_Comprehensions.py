a = [1, 3, 5, 7, 9, 11]  # [2, 6, 10, 14, 18, 22]
b = []
b.append(10)    # .append()
b.append(20)
b.append(25)
print(b)

c = []
for x in a:
    c.append(x *2)
print(c)

d = [x * 2 for x in a]
print(d)

# [1, 4, 9, 16, 25, 36]
e1 = []
for x in range(1, 7):
    e1.append(x ** 2)
print(e1)

e2 = [x ** 2 for x in range(1, 7)]
print(e2)

# [36, 25, 16, 9, 4, 1]
f1 = []
for x in range(6, 0, -1):
    f1.append(x ** 2)
print(f1)

f2 = [x ** 2 for x in range(6, 0, -1)]
print(f2)

