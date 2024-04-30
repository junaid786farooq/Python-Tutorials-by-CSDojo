# program to calculate the sum of all even numbers from 1 to 100 using the range() function.

sum_of_even = 0

for num in range(2, 101, 2):
    sum_of_even += num

print("Sum of all even numbers from 1 to 100 is:", sum_of_even)