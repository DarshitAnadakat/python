def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero")
    else:
        print(f"Result: {result}")
    finally:
        print("Function execution completed")


divide_numbers(10, 2) 
divide_numbers(10, 0) 
