dict = {}
dict["Junaid"] = 21
dict["Usman"] = 20
dict["Mudasir"] = 20
dict["waqas"] = 23


print(dict["Mudasir"])
print(dict["Junaid"])

print(dict.keys())
print(dict.values())
print(dict.items())
print(dict.get("Ali"))

# Keys are commonly strings or numbers

dict[10] = 100
print(dict[10])

# How to iterate over key-value pairs?
for key, value in dict.items():
    print("Key")
    print(key)
    print("Value")
    print(value)
