# A set is a type of data that stores a set of things.

a = set()
print(a)

a.add(1)
a.add(2)
a.add(2)
print(a)

for x in a:
    print(x)

given_list1 = [1, 1, 2, 4, 2]
new_set = set()
for x in given_list1:
    new_set.add(x)
print(new_set)

new_list1 = list()
for x in new_set:
    new_list1.append(x)
print(new_list1)

b = set()
b.add('apple')
b.add('banana')
b.add(1)
print(b)

given_list2 = [1, 3, 4, 1, 3]
new_set2 = set()
for x in given_list2:
    new_set2.add(x)
total = 0
for x in new_set2:
    total += x
print(total) 