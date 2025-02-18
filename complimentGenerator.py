import random

# Predefined list of compliments
compliments = [
    "You have a great sense of humor!",
    "Your smile lights up the room.",
    "You are so thoughtful and kind.",
    "You have a brilliant mind!",
    "You're an amazing friend!",
]

# Function to display a random compliment
def random_compliment():
    compliment = random.choice(compliments)  # Randomly select a compliment
    print(f"\n🌟 Here's your compliment: {compliment}")

# Function to add a new compliment
def add_compliment():
    new_compliment = input("\nEnter a new compliment to add: ").strip()
    if new_compliment:
        compliments.append(new_compliment)
        print("Your compliment has been added! 😊")
    else:
        print("No compliment entered. Returning to the menu.")

# Main menu
def display_menu():
    while True:
        print("\nCompliment Generator Menu:")
        print("1. Get a random compliment")
        print("2. Add a new compliment")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ").strip()
        if choice == "1":
            random_compliment()
        elif choice == "2":
            add_compliment()
        elif choice == "3":
            print("Goodbye! Spread kindness! 🌼")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    display_menu()
