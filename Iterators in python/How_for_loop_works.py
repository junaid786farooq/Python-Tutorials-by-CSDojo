num = [1,2,3]

# # fetch the iterator
# iter_num = iter(num)

# # step2 --> next
# print(next(iter_num))
# print(next(iter_num))
# print(next(iter_num))
# print(next(iter_num))


# ## Making our own for loop

# def my_own_for_loop(iterable):
#     iterator = iter(iterable)
#     while True:
#         try:
#             print(next(iterator))
#         except StopIteration:
#             break

# a = [1,2,3]
# b = range(1, 11)
# c = (1,2,3)
# d = {1,2,3}
# e = {0:1, 1:1}

# my_own_for_loop(a)
# my_own_for_loop(b)
# my_own_for_loop(c)
# my_own_for_loop(d)
# my_own_for_loop(e)

# ## A confusing point
# num = [1,2,3]
# iter_obj = iter(num)
# print(id(iter_obj), "Address of iterator 1")

# iter_obj2 = iter(iter_obj)
# print(id(iter_obj2), "Address of iterator 2")


## Let's create our own range function
class My_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __iter__(self):
        return My_range_iterator(self)
    
    
class My_range_iterator:
    def __init__(self, iterable_obj):
        self.iterable = iterable_obj
    def __iter__(self):
        return self
    def __next__(self):
        if self.iterable.start >= self.iterable.end:
            raise StopIteration
        current = self.iterable.start 
        self.iterable.start += 1
        return current
    
x = My_range(1, 11)
print(type(x))
print(iter(x))
for i in My_range(1, 11):
    print(i)