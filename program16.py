import math

n = int(input("Enter a number: "))

sqrt_list = []

for num in range(1, n+1):
    sqrt = math.sqrt(num)
    sqrt_list.append(sqrt)

print("List of square roots of numbers between 1 and", n, ":")
print(sqrt_list)