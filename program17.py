import math

n = int(input("Enter a number: "))

sqrt_dict = {}

for num in range(1, n+1):
    sqrt = math.sqrt(num)
    sqrt_dict[num] = sqrt

print("Dictionary of numbers and their square roots between 1 and", n, ":")
print(sqrt_dict)