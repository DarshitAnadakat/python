def is_prime(num):
    if num < 2:
        return False
    
    if num == 2:
        return True
    
    for i in range(3, int(num**0.5)+1, 2):
        if num % i == 0:
            return False
    
    return True

num = int(input("Enter a number: "))

if is_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
