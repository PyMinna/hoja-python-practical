try:

    number = int(input("Enter a number: "))
    result = number ** 2
    print(result)

except ValueError:

    print("Enter a valid number.")

else:
    
    print("Calculation successfull.")