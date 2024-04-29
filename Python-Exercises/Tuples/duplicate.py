# program that takes a tuple of integers as input from the user and checks if the tuple contains any duplicate elements, then prints "Duplicates found" or "No duplicates found" accordingly.

tup = tuple(map(int, input("Enter numbers with spaces: ").split()))

tup_dupli = False

for i in range(len(tup)):
    for j in range(i + 1, len(tup)):
        if tup[i] == tup[j]:
            tup_dupli = True
            break

if tup_dupli:
    print("Duplicates found")
else:
    print("No duplicates found")
