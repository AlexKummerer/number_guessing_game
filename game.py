from constants import (
    WELCOME_MESSAGE,
    GOODBYE_MESSAGE,
    INVALID_CHOICE_MESSAGE,
    PLAY_AGAIN_PROMPT,
)
from levels import easy_level, medium_level, hard_level


def play_again():
    """Prompts the user to play again or exit the game."""
    while True:
        response = input(PLAY_AGAIN_PROMPT).strip().lower()
        if response == "yes":
            return True  # User wants to play again
        elif response == "no":
            return False  # User wants to choose a new level
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


def get_user_choice(level_options):
    """Get user choice from the given level options."""
    print("\nChoose a level:")
    for key, (description, _) in level_options.items():
        print(f"{key}. {description}")

    user_choice = input("Enter the number corresponding to your choice: ").strip()
    return user_choice


def handle_user_choice(user_choice, level_options):
    """Handle the user choice based on the given level options."""
    if user_choice in level_options:
        description, function = level_options[user_choice]
        if function is None:
            print(GOODBYE_MESSAGE)
            return False  # Signal to exit the game
        else:
            print(f"You have chosen {description} level.")
            function()  # Call the corresponding level function

            if not play_again():
                # User chose 'no' to play again, go back to level selection
                return True
    else:
        print(INVALID_CHOICE_MESSAGE)
        return True


def main():
    """Main function to start the game and handle user level selection."""
    print(WELCOME_MESSAGE)

    # Dictionary mapping user choices to level descriptions and functions
    level_options = {
        "1": ("Easy", easy_level),
        "2": ("Medium", medium_level),
        "3": ("Hard", hard_level),
        "0": ("Exit", None),
    }

    while True:
        user_choice = get_user_choice(level_options)
        continue_game = handle_user_choice(user_choice, level_options)
        if not continue_game:
            break  # Exit the game


# Start the game
if __name__ == "__main__":
    main()
