# Compute all multiples of 3 and 5. That are less than 100.

total = 0
for i in range(1, 101):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print("Compute of multipe of 3, 5 is:",total)