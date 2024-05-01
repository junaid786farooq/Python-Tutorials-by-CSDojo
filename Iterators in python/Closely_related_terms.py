# # Iteration
# num = [1, 2, 3]
# for i in num:
#     print(i)

# # Iterator
# l = [x for x in range(1, 100001)]
# # for i in l:
# #     print(i * 2)
# import sys
# print(sys.getsizeof(l)) 
# x = range(1, 100000001)
# # for i in x:
# #     print(i * 2)
# print(sys.getsizeof(x))

# # Iterable
# l = [1,2,3]
# print(type(l))  # l is an iterable
# print(type(iter(l)))  # iter(l) is --> iterator


# # Trick
# # if we can drove loop then this is iterable
# # if we see iter method in list of dir then this is iterable
# a = 2
# # for i in a:
# #     print(i)
# print(dir(a))

# T = (1,2,3)
# print(dir(T)) # --> iter method show so this is iterable

# S = {1,2,3}
# print(dir(S)) # --> iter method show so this is iterable

# D = {1:2,3:4}
# print(dir(D)) # --> iter method show so this is iterable 


# For checking iterator
# Drove dir on it if we find iter and next both methods then this is iterator
L = [1,2,3]
# L is not an iterator
iter_L = iter(L) # iter_L is an iterator
print(dir(L))