def calculator():
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Exponentiation (**)")
    print("7. Floor Division (//)")
    
    # Take input from the user
    choice = input("Enter the number corresponding to the operation (1-7): ")
    
    # Validate the choice
    if choice not in ['1', '2', '3', '4', '5', '6', '7']:
        print("Invalid choice! Please try again.")
        return

    # Take numbers as input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Perform the chosen operation
    if choice == '1':
        print(f"Result: {num1} + {num2} = {num1 + num2}")
    elif choice == '2':
        print(f"Result: {num1} - {num2} = {num1 - num2}")
    elif choice == '3':
        print(f"Result: {num1} * {num2} = {num1 * num2}")
    elif choice == '4':
        if num2 != 0:
            print(f"Result: {num1} / {num2} = {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed!")
    elif choice == '5':
        print(f"Result: {num1} % {num2} = {num1 % num2}")
    elif choice == '6':
        print(f"Result: {num1} * {num2} = {num1 ** num2}")
    elif choice == '7':
        if num2 != 0:
            print(f"Result: {num1} // {num2} = {int(num1 // num2)}")  # Ensure integer result
        else:
            print("Error: Division by zero is not allowed!")
    else:
        print("Invalid input.")

# Run the calculator
calculator()
