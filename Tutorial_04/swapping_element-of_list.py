fruit = ["banana", "apple", "graps"]
print(fruit)

temp_variable = fruit[0]
fruit[0]  = fruit[2]
fruit[2] = temp_variable
print(fruit)

# # OR For reverse the list we use method.

# reverse_list = fruit.reverse()
# print(fruit)