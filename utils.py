import random
from constants import (
    DEFAULT_START_RANGE,
    DEFAULT_END_RANGE,
    INVALID_NUMBER_MESSAGE,
    RANGE_PROMPT_START,
    RANGE_PROMPT_END,
    RANGE_ERROR_MESSAGE,
)


def generate_a_number(start_range=DEFAULT_START_RANGE, end_range=DEFAULT_END_RANGE):
    """Generates a random number between start_range and end_range."""
    return random.randint(start_range, end_range)


def guess_the_number(prompt):
    """Prompts the user to guess a number and handles invalid input."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(INVALID_NUMBER_MESSAGE)


def user_sets_range():
    """Allows the user to set the guessing range with validation."""
    while True:
        start_range = guess_the_number(RANGE_PROMPT_START)
        end_range = guess_the_number(RANGE_PROMPT_END)
        if start_range < end_range:
            return start_range, end_range
        else:
            print(RANGE_ERROR_MESSAGE)
