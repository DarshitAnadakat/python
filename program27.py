filename = input("Enter the filename: ")

with open(filename, "r") as file:
    for line in file:
        print(line.strip())
