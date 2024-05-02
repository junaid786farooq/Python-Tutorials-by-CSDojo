# program that reads the contents of a text file named "input.txt", searches for a specific word (e.g., "old_word"), replaces it with another word (e.g., "new_word"), and then writes the modified contents to another file named "output.txt".

with open("input.txt", "r") as input_file:
    with open("output2.txt", "w") as output2_file:
        for line in input_file:
            new_line = line.replace("web", "Website")
            output2_file.write(new_line)

with open("output2.txt", "r") as file:
    data = file.read()
    print(data)