from constants import WELCOME_MESSAGE, GOODBYE_MESSAGE, INVALID_CHOICE_MESSAGE, PLAY_AGAIN_PROMPT
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
        print("\nChoose a level:")
        for key, (description, _) in level_options.items():
            print(f"{key}. {description}")

        user_choice = input("Enter the number corresponding to your choice: ").strip()
        if user_choice in level_options:
            description, function = level_options[user_choice]
            if function is None:
                print(GOODBYE_MESSAGE)
                break  # Exit the game
            else:
                print(f"You have chosen {description} level.")
                function()  # Call the corresponding level function

                if not play_again():
                    # User chose 'no' to play again, go back to level selection
                    continue
        else:
            print(INVALID_CHOICE_MESSAGE)


# Start the game
if __name__ == "__main__":
    main()
