# Initialize the grades dictionary
grades = {}

# Function to display the menu
def display_menu():
    print("\nStudent Grades Tracker Menu:")
    print("1. Add Student and Grade")
    print("2. View All Students and Grades")
    print("3. Edit Student Grade")
    print("4. Delete Student Grade")
    print("5. Calculate Class Statistics")
    print("6. Exit")

# Function to add a grade
def add_grade(grades):
    student_name = input("\nEnter the student's name: ").strip()

    # Check for duplicate entries
    if student_name in grades:
        overwrite = input(f"{student_name} already exists. Do you want to overwrite their grade? (yes/no): ").lower()
        if overwrite != "yes":
            print("Operation canceled.")
            return

    while True:
        try:
            grade = float(input(f"Enter {student_name}'s grade (0-100): "))
            if 0 <= grade <= 100:
                break
            else:
                print("Grade must be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric value for the grade.")

    grades[student_name] = grade
    print(f"\n{student_name}'s grade has been added/updated successfully.")

# Function to view all grades
def view_all_grades(grades):
    if not grades:
        print("\nNo students or grades available.")
    else:
        print("\nAll Students and Grades:")
        for student, grade in grades.items():
            print(f"- {student}: {grade}")

# Function to edit a grade
def edit_grade(grades):
    student_name = input("\nEnter the name of the student whose grade you want to edit: ").strip()
    if student_name not in grades:
        print(f"{student_name} is not in the list.")
        return

    while True:
        try:
            grade = float(input(f"Enter the new grade for {student_name} (0-100): "))
            if 0 <= grade <= 100:
                grades[student_name] = grade
                print(f"\n{student_name}'s grade has been updated to {grade}.")
                break
            else:
                print("Grade must be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Function to delete a grade
def delete_grade(grades):
    student_name = input("\nEnter the name of the student whose grade you want to delete: ").strip()
    if student_name in grades:
        del grades[student_name]
        print(f"\n{student_name}'s grade has been removed.")
    else:
        print(f"{student_name} is not in the list.")

# Function to calculate class statistics
def calculate_class_statistics(grades):
    if not grades:
        print("\nNo grades available to calculate statistics.")
        return

    total_students = len(grades)
    total_grades = sum(grades.values())
    average = total_grades / total_students
    highest = max(grades.values())
    lowest = min(grades.values())

    print("\nClass Statistics:")
    print(f"- Total Students: {total_students}")
    print(f"- Average Grade: {average:.2f}")
    print(f"- Highest Grade: {highest}")
    print(f"- Lowest Grade: {lowest}")

# Main program loop
def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_grade(grades)
        elif choice == "2":
            view_all_grades(grades)
        elif choice == "3":
            edit_grade(grades)
        elif choice == "4":
            delete_grade(grades)
        elif choice == "5":
            calculate_class_statistics(grades)
        elif choice == "6":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please select a valid option.")

# Run the program
if __name__ == "__main__":
    main()
