def calculator():
    try:

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        op =input("Select operator('+','-','*','/','%'): ")

        if op == '+':
            print("Result = ", a + b)
        elif op == '-':
            print("Result = ", a - b)
        elif op == '*':
            print("Result = ", a * b)
        elif op == '/':
            print("Result = ", a / b)
        elif op == '%':
            print("Result = ", a % b)
        else:
            raise ValueError("Invalid operator!, Please try again.")
        
        
    except ValueError as e:

        print("Error: ", e)

    except ZeroDivisionError:
    
        print("Error: Division by zero not allowed. ")

    else:
        print("Calculation Successfull!.")

    finally:

        print("Thankyou for using the calculator.")


calculator()