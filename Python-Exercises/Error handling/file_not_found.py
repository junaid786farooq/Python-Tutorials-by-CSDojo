# program that tries to open a file named "dalta.txt" for reading. Implement error handling to catch the FileNotFoundError if the file does not exist and print a message to the user.

try:
    with open("dalta,txt", "r") as file:
        content = file.read()
        print("File content:", content)
except FileNotFoundError:
    print("Error: Your file is not found...!")