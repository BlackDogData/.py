# Habit Tracker
habits = []

def display_menu():
    print("\nHabit Tracker")
    print("1. Add a habit")
    print("2. View habits")
    print("3. Mark a habit as completed")
    print("4. Exit")

running = True
while running:
    display_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        habit = input("Enter the habit you want to track: ")
        habits.append({"name": habit, "completed": False})
        print(f"Habit '{habit}' added!")
    elif choice == "2":
        if not habits:
            print("No habits to show!")
        else:
            print("\nYour habits:")
            for i, habit in enumerate(habits, start=1):
                status = "✔" if habit["completed"] else "✘"
                print(f"{i}. {habit['name']} - {status}")
    elif choice == "3":
        if not habits:
            print("No habits to mark!")
        else:
            print("\nWhich habit did you complete?")
            for i, habit in enumerate(habits, start=1):
                print(f"{i}. {habit['name']}")
            try:
                habit_num = int(input("Enter the number of the habit: "))
                if 1 <= habit_num <= len(habits):
                    habits[habit_num - 1]["completed"] = True
                    print(f"Habit '{habits[habit_num - 1]['name']}' marked as completed!")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a valid number.")
    elif choice == "4":
        print("Goodbye!")
        running = False
    else:
        print("Invalid choice. Please try again.")
