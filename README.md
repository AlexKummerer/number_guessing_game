# Number Guessing Game

Welcome to the Number Guessing Game! This is a fun command-line game where players try to guess a randomly generated number within a specified range. The game offers three levels of difficulty: Easy, Medium, and Hard.

## Table of Contents

- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [How to Play](#how-to-play)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

The project is organized into several files for better modularity and maintainability:

- `game.py`: The main entry point for the game. It handles the game loop and user interaction.
- `levels.py`: Contains the logic for each game level (Easy, Medium, and Hard).
- `utils.py`: Includes utility functions such as generating random numbers and validating user input.
- `constants.py`: Stores constants and messages used throughout the game.

## Features

- **Easy Level**: Guess a number between 1 and 10.
- **Medium Level**: Set your own range and guess the number within that range with unlimited attempts.
- **Hard Level**: Set your own range, guess the number, but with a limited number of attempts based on the range size.
- **User-Friendly**: Provides hints and feedback after each guess.
- **Replay Option**: After each game, you can choose to play again or select a different level.

## Installation

To get started with the Number Guessing Game, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/number-guessing-game.git
2. Navigate to the Project Directory:
  cd number-guessing-game
3. Ensure you have Python Installed:
  This project requires Python 3.6 or higher. You can download Python from python.org.

Usage
To start the game, simply run the game.py file:
python game.py
Follow the on-screen prompts to choose a difficulty level and start playing.

How to Play
Start the Game: Run game.py and follow the instructions to choose a level:

Easy: Guess a number between 1 and 10.
Medium: Set your own range and guess the number.
Hard: Set your own range and guess the number with a limited number of attempts.
Make Guesses: Enter your guesses based on the hints provided (Too low, Too high).

Winning: If you guess the correct number, you win! The number of attempts taken will be displayed.

Replay or Exit: After the game ends, choose whether to play again or exit.

Contributing
Contributions are welcome! Here’s how you can help:

Fork the repository.
Create a new branch for your feature or bugfix:

git checkout -b feature/your-feature-name
Make your changes and commit them:

git commit -m 'Add some feature'
Push your changes to your fork:

git push origin feature/your-feature-name
Open a pull request describing the changes you made.


License
This project is licensed under the MIT License - see the LICENSE file for details.
