# Creates two empty lists.
income_list = []
expense_list = []

# Defines the function that creates the menu
def display_menu():
    print("\nBudget Tracker Menu:")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Income and Expenses")
    print("4. Quit")


running = True
while running:
    display_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        print("Add Income")
        try:
            amount = float(input("Enter the income amount: $"))
            income_list.append(amount)
            print("Income added successfully!")
        
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
    
    elif choice == "2":
        print("Add Expense")
        try:
            amount = float(input(f"Enter the expense amount: $"))
            expense_list.append(amount)
            print(f"Expense added successfully!")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
    
    elif choice == "3":
        print("View Income and Expenses")
        total_income = sum(income_list)
        total_expenses = sum(expense_list)
        print(f"Total Income: ${total_income}")
        print(f"Total Expenses: ${total_expenses}")
        balance = total_income - total_expenses
        print(f"Balance: ${balance}")
        
        if balance < 0:
            print("Warning: You are over budget!")
    
    elif choice == "4":
        print("Goodbye!")
        running = False
    
    else:
        print("Invalid choice. Please try again.")