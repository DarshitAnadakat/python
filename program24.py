lines = []

while True:
    line = input("Enter a sentence (or a blank line to exit): ")
    
    if line == "":
        break
    
    capitalized_line = line.upper()
    
    lines.append(capitalized_line)

print("Capitalized sentences:")
for line in lines:
    print(line)
