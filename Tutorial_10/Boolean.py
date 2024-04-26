print(type("microsoft"))
print(type(4))
print(type(True))

a = 3
b = 1
if a > b:
    print("a is greater than b.")

if True:
    print("a is greater than b")

boolean_value = a > b
print(boolean_value)

if boolean_value:
    print("a is greater than b.")

def are_you_sad(is_rainy, has_umberlla):
    return is_rainy and not has_umberlla
print(are_you_sad(True, False))
print(are_you_sad(False, True))

def c_greater_than_d_plus_e(c, d, e):
    return c > d + e
print(c_greater_than_d_plus_e(9,3,2))
print(c_greater_than_d_plus_e(9,3,7))