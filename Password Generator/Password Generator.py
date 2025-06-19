import string
import random

def get_user_choice(prompt: str) -> bool:
    while True:
        choice = input(prompt).strip().lower()
        if choice in ['y', 'n']:
            return choice == 'y'
        print("Invalid input. Please enter 'y' or 'n'.")

def get_password_length() -> int:
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length > 0:
                return length
            print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def generate_password(length: int, use_letters: bool, use_numbers: bool, use_symbols: bool) -> str:
    character_pool = ""
    if use_letters:
        character_pool += string.ascii_letters
    if use_numbers:
        character_pool += string.digits
    if use_symbols:
        character_pool += "!@#$%&*"

    if not character_pool:
        raise ValueError("No character types selected.")

    return ''.join(random.choice(character_pool) for _ in range(length))

def main():
    print("=== Password Generator ===\n")
    while True:
        use_letters = get_user_choice("Include letters? (y/n): ")
        use_numbers = get_user_choice("Include numbers? (y/n): ")
        use_symbols = get_user_choice("Include symbols? (y/n): ")

        if not (use_letters or use_numbers or use_symbols):
            print("You must select at least one character type.\n")
            continue

        length = get_password_length()

        try:
            password = generate_password(length, use_letters, use_numbers, use_symbols)
            print(f"\nGenerated Password: {password}\n")
        except ValueError as e:
            print(f"Error: {e}")
            continue

        if not get_user_choice("Generate another password? (y/n): "):
            print("See You!")
            break

if __name__ == "__main__":
    main()