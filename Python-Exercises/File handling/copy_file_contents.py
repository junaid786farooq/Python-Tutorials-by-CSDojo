# program that reads the contents of a file named "source.txt" and copies them to another file named "destination.txt".

with open("source.txt", 'w') as file:
    file.write("Artificial Intelligence (AI) is a branch of computer science\nThat aims to create intelligent machines capable of performing tasks\nThat typically require human intelligence.\nThese tasks include:\nLearning\nReasoning\nProblem-solving\nperception, and language understanding.\nAI has rapidly advanced in recent years, revolutionizing industries and transforming the way we live and work.")

with open("source.txt", "r") as firstfile, open("destination.txt", "a") as secondfile:
    for line in firstfile:
        secondfile.write(line)
    
with open("destination.txt", "r") as file:
    contents = file.read()
    print(contents)