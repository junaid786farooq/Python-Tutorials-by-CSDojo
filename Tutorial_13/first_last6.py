# Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.
'''
first_last6([1, 2, 6]) → True
first_last6([6, 1, 2, 3]) → True
first_last6([13, 6, 1, 2, 3]) → False
'''

def first_last6(numbers):
    if numbers[0] == 6 or numbers[-1] == 6:
        return True
    else:
        return False
    
print(first_last6([1,2,3,4,5,6]))