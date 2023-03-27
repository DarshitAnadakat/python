principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
years = float(input("Enter the time period in years: "))

interest = principal * (pow((1 + rate / 100), years)) - principal

print("Compound interest = ", interest)