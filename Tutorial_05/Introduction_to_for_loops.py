a = ["banana", "apple", "microsoft"]
for element in a:
    print(element)
    print(element)

b = [20, 10, 5]
total = 0
for e in b:
    total = total + e
print(total)

# 1, 2, 3, 4
c = list(range(1, 5))
print(c)

total2 = 0
for i in range(1, 5):
    total2 += i
print(total2) 

print(list(range(1, 8)))

print(7 % 3) # modulo operator give reminder

total3 = 0
for i in range(1, 8):
    if i % 3 == 0:
        total3 += i
print(total3)
