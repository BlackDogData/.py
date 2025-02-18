import random
import string

def generate_password():
    print("Welcome to the Password Generator")
    length = int(input("Enter the length of the password: "))

    # Define character pools
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Initialize an empty pool
    char_pool = ""

    # Ask user for preferences
    include_lower = input("Include lowercase letters? (Yes/No): ").strip().lower()
    if include_lower == "yes":
        char_pool += lower

    include_upper = input("Include uppercase letters? (Yes/No): ").strip().lower()
    if include_upper == "yes":
        char_pool += upper

    include_digits = input("Include digits? (Yes/No): ").strip().lower()
    if include_digits == "yes":
        char_pool += digits
    
    include_symbols = input("Include symbols? (Yes/No): ").strip().lower()
    if include_symbols == "yes":
        char_pool += symbols
    
    # Ensure pool is empty
    if not char_pool:
        print("You must include at least one character type!")
        return
    
    # Generate password
    password = ''.join(random.choice(char_pool) for _ in range(length))
    print(f"Your generated password is: {password}")