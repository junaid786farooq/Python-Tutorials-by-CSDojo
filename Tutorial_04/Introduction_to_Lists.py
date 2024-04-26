a = [3, 10, -1]
print(a)

a.append(1)
a.append("Hello")
a.append([1, 2])
print(a)

a.pop()
a.pop()
print(a)

print(a[0])
print(a[3])
print(a[-2])

a[0] = 100
print(a)