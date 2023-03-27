def factorial(n):
    """Calculates the factorial of the given number n using recursion."""
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a number to find its factorial: "))

result = factorial(num)

print(num, "! =", result)
