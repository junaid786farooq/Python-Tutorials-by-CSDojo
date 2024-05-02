# program that prompts the user to enter multiple lines of text, then writes these lines to a file named "output.txt".

with open("output.txt", "w") as file:
    while True:
        line = input("Enter a line (or press enter to stop): ")    
        if not line:
            break
        file.write(line + "\n")


with open("output.txt", "r") as file:
    content = file.read()
    print(content)