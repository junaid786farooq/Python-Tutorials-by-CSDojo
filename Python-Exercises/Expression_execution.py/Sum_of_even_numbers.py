# program that calculates the sum of all even numbers from 1 to 100 using a loop.

sum_of_even_num = 0

for i in range(1, 101):
    if i % 2 == 0:
        sum_of_even_num += i

print("The sum of all even numbers from 1 to 100 is:", sum_of_even_num)