def calculate(num1, num2, op):
    """Calculates the result of applying the given arithmetic operator to the two numbers."""
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 / num2
    else:
        return None

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
op = input("Enter the arithmetic operator (+, -, *, /): ")

result = calculate(num1, num2, op)

if result is None:
    print("Invalid operator.")
else:
    print(num1, op, num2, "=", result)
