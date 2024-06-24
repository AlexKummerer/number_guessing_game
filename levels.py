from utils import generate_a_number, guess_the_number, user_sets_range
from constants import (
    EASY_LEVEL_MAX,
    MAX_ATTEMPTS_FACTOR,
    GUESS_PROMPT,
    GUESS_PROMPT_MEDIUM,
)


def compare_the_numbers(user_guess, number_to_guess, attempts):
    """Compares the user's guess to the number to guess and provides feedback."""
    if user_guess < number_to_guess:
        print("Too low! Try again.")
        return False
    elif user_guess > number_to_guess:
        print("Too high! Try again.")
        return False
    else:
        print(
            f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts."
        )
        return True


def play_game(number_to_guess, max_attempts=None, prompt=GUESS_PROMPT):
    """Handles the main game loop for guessing the number."""
    attempts = 0
    while True:
        user_guess = guess_the_number(prompt)
        attempts += 1
        if compare_the_numbers(user_guess, number_to_guess, attempts):
            break
        if max_attempts is not None:
            remaining_attempts = max_attempts - attempts
            if remaining_attempts <= 0:
                print(
                    f"Sorry, you've used all {max_attempts} attempts. The correct number was {number_to_guess}."
                )
                break
            else:
                print(f"You have {remaining_attempts} attempts left.")


def easy_level():
    """Handles the game logic for the easy level."""
    number_to_guess = generate_a_number(end_range=EASY_LEVEL_MAX)
    play_game(number_to_guess)


def medium_level():
    """Handles the game logic for the medium level."""
    start_range, end_range = user_sets_range()
    number_to_guess = generate_a_number(start_range, end_range)
    play_game(number_to_guess, prompt=GUESS_PROMPT_MEDIUM)


def hard_level():
    """Handles the game logic for the hard level."""
    start_range, end_range = user_sets_range()
    number_to_guess = generate_a_number(start_range, end_range)
    range_size = end_range - start_range
    max_attempts = max(
        1, int(range_size * MAX_ATTEMPTS_FACTOR)
    )  # Ensure at least 1 attempt
    print(f"You have a maximum of {max_attempts} guesses!")
    play_game(number_to_guess, max_attempts, prompt=GUESS_PROMPT_MEDIUM)
