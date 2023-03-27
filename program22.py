string = input("Enter a comma-separated string: ")

tokens = string.split(',')
print("Tokens using split():", tokens)

tokens = string.rsplit(',', 1)
print("Tokens using rsplit():", tokens)

tokens = string.splitlines()
print("Tokens using splitlines():", tokens)
