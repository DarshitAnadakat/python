filename = input("Enter the filename: ")

with open(filename, "r") as file:
    numbers = []
    for line in file:
        number = float(line.strip())
        numbers.append(number)

total = sum(numbers)
average = total / len(numbers)

print("Numbers:", numbers)
print("Total:", total)
print("Average:", average)
