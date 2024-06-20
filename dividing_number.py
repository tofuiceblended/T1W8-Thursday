def divide_numbers():
    try:
        # Get input from the user
        dividend = float(input("Enter the dividend: "))
        divisor = float(input("Enter the divisor: "))
        
        # Perform the division
        result = dividend / divisor
        print(f"Result of division is {result}")

    except ZeroDivisionError:
        print("Error! Division by zero is not allowed.")
    except ValueError:
        print("Error! please enter valid numbers")
    except Exception as e:
        print(f"An unexpected error occured: {e}")
    finally:
        print("Division operation closed.")

# Perform the division
print(divide_numbers())