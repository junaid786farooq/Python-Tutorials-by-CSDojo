# Program to calculate the sum of all the negative numbers in the list.

# given_list = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]
# total = 0
# for element in given_list:
#     if element <= 0:
#         total += element
# print(total)

given_list = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]
total2 = 0
i = 0
while i < len(given_list):
    if given_list[i] < 0:
        total2 += given_list[i]
    i += 1
print(total2)       