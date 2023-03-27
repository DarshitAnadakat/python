num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an arithmetic operator (+, -, *, /): ")

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    print("Invalid operator!")
    exit()

print("Result: ", result)