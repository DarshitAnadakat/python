def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

num = int(input("Enter a number: "))

fact = factorial(num)

print("Factorial of", num, "is", fact)