# program that includes comments to clarify the logic behind a particular algorithm or loop.

# This program finds the sum of all even numbers from 1 to 10
total = 0

# Running loop from 1 to 10
for i in range(1, 11):

  # Check if the number is even 
    if i % 2 == 0:

      # Add the even number to the total
        total += i

# print the sum of even numbers
print("Sum of all even numbers from 1 to 10 is:",total)