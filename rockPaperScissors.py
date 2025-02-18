import random  # Importing the random module for generating computer's choice

# Welcome message
print("\nWelcome to Rock, Paper, Scissors!")
print("\nRules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.")

# List of possible choices
choices = ["rock", "paper", "scissors"]

# Initialize scores
user_wins = 0
computer_wins = 0
ties = 0

# Main game loop
while True:
    # User's move
    user_choice = input("\nEnter your choice (rock, paper, scissors or quit): ").strip().lower()
    
    # Check if the user wants to quit
    if user_choice == "quit":
        print("\nThanks for playing! Here's the final score:")
        print(f"You: {user_wins} | Computer: {computer_wins} | Ties: {ties}")
        break

    # Validate user's choice
    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        continue

    # Computer's move
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
        ties += 1  # Increment tie score
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
        user_wins += 1  # Increment user's score
    else:
        print("You lose!")
        computer_wins += 1  # Increment computer's score

    # Display the current score
    print(f"Score: You: {user_wins} | Computer: {computer_wins} | Ties: {ties}")
