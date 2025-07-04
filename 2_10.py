def display_menu():
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

while True:
    display_menu()
    choice = input("Enter choice (1/2/3/4/5): ")
    if choice == '5':
        print("Exiting program!")
        break
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.\n")
            continue
        if choice == '1':
            result = num1 + num2
            print(f"Result: {num1} + {num2} = {result}\n")
        elif choice == '2':
            result = num1 - num2
            print(f"Result: {num1} - {num2} = {result}\n")
        elif choice == '3':
            result = num1 * num2
            print(f"Result: {num1} * {num2} = {result}\n")
        elif choice == '4':
            if num2 != 0:
                result = num1 / num2
                print(f"Result: {num1} / {num2} = {result}\n")
            else:
                print("Error: Division by zero is not allowed.\n")
    else:
        print("Invalid choice. Please select a valid option.\n")