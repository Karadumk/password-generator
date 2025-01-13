import random
import string

# Define our character sets
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation


def generate_password(length, use_digits=True, use_special=True):

    # Initialize our character pools
    all_chars = string.ascii_letters  # Always include letters
    required_chars = [random.choice(string.ascii_letters)]  # Ensure at least one letter

    # Build our character pools and requirements
    if use_digits:
        all_chars += string.digits
        required_chars.append(random.choice(string.digits))
    if use_special:
        all_chars += string.punctuation
        required_chars.append(random.choice(string.punctuation))

    # Check for valid inputs
    if len(required_chars) > length:
        raise ValueError(
            "Password length must be at least as long as the number of required character types"
        )

    # Generate the remaining characters
    remaining_length = length - len(required_chars)
    remaining_chars = [random.choice(all_chars) for _ in range(remaining_length)]

    # Combine all characters and shuffle
    all_password_chars = required_chars + remaining_chars
    random.shuffle(all_password_chars)

    return "".join(all_password_chars)


def main():
    print("Welcome to Password Generator!")
    print("Enter 'q' at any time to quit the program.")
    
    while True:  # Main program loop
        # Get password length
        length_input = input("\nHow long should the password be? ")
        
        # Check if user wants to quit
        if length_input.lower() == 'q':
            print("Thank you for using Password Generator. Goodbye!")
            break
            
        # Validate length input
        try:
            length = int(length_input)
            if length < 1:
                print("Please enter a positive number for password length.")
                continue
        except ValueError:
            print("Please enter a valid number for password length.")
            continue
        
        # Get character type preferences
        digits_input = input("Include numbers? (y/n): ").lower()
        if digits_input == 'q':
            print("Thank you for using Password Generator. Goodbye!")
            break
        use_digits = digits_input == 'y'
        
        special_input = input("Include special characters? (y/n): ").lower()
        if special_input == 'q':
            print("Thank you for using Password Generator. Goodbye!")
            break
        use_special = special_input == 'y'
        
        # Generate and display password
        try:
            password = generate_password(length, use_digits, use_special)
            print("\nYour generated password is:", password)
            
            # Ask if user wants to generate another password
            again = input("\nGenerate another password? (y/n): ").lower()
            if again != 'y':
                print("Thank you for using Password Generator. Goodbye!")
                break
                
        except ValueError as e:
            print("\nError:", str(e))

if __name__ == "__main__":
    main()
