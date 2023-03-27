principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
years = float(input("Enter the time period in years: "))

interest = (principal * rate * years) / 100

print("Simple interest = ", interest)