filename = input("Enter the filename: ")

with open(filename, "w") as file:
    while True:
        name = input("Enter a name (or press Enter to quit): ")
        if name == "":
            break
        file.write(name + "\n")

print("Names saved to", filename)
