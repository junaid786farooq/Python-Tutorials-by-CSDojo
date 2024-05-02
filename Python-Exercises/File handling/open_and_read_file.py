# program to open a text file named "sample.txt", read its contents, and print them to the console.

with open("sample.txt", "w") as f:
    data = f.write("Hi...\nI am learning python.")


with open("sample.txt", "r") as file:
    content = file.read()
    print(content)
