# function called average that calculates the average of a variable number of arguments. The function should return the average of all the arguments passed to it. Test the function with different numbers of arguments.

def average(*args):
    if len(args) == 0:
        return None
    total=  sum(args)
    return total / len(args)


print("Average", average(1,2,3,4,5))
print(average())