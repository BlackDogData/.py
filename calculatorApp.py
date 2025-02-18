def display_menu():
    print("\nWelcome to the Python Calculator!")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Quit")

def get_user_choice():
    while True:
        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice in range(1, 6):
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def perform_calculation(choice):
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        if choice == 1:
            print(f"The result is: {num1 + num2}")
        elif choice == 2:
            print(f"The result is: {num1 - num2}")
        elif choice == 3:
            print(f"The result is: {num1 * num2}")
        elif choice == 4:
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                print(f"The result is: {num1 / num2}")
    except ValueError:
        print("Invalid input. Please enter numbers only.")

def calculator():
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == 5:
            print("Thank you for using the calculator. Goodbye!")
            break
        
        perform_calculation(choice)

# Run the calculator
calculator()
