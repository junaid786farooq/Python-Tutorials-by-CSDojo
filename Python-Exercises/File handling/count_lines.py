# program to open a text file named "data.txt", count the number of lines in the file, and print the count to the console.

with open("data.txt", "w") as file:
    data = file.write("Hi, everyone!\nMy name is Junaid.\nI am a software engineering student.\nStudying at IUB.")


with open("data.txt", "r") as file:
    count_line = sum(1 for line in file)
    print("Number of lines:", count_line)