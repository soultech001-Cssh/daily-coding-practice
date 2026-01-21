#!/usr/bin/env python3
"""
Number Guessing Game
Try to guess the secret number between 1 and 1000!
"""

import random


def play_game():
    """Play a round of the number guessing game."""
    secret_number = random.randint(1, 1000)
    attempts = 0
    max_attempts = 10  # With binary search, 10 attempts is enough for 1-1000

    print("\n" + "=" * 50)
    print("Welcome to the Number Guessing Game!")
    print("=" * 50)
    print(f"\nI'm thinking of a number between 1 and 1000.")
    print(f"You have {max_attempts} attempts to guess it.")
    print("Tip: Use binary search strategy for best results!\n")

    while attempts < max_attempts:
        attempts += 1
        remaining = max_attempts - attempts

        try:
            guess = int(input(f"Attempt {attempts}/{max_attempts} - Enter your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            attempts -= 1  # Don't count invalid input as an attempt
            continue

        if guess < 1 or guess > 1000:
            print("Please guess a number between 1 and 1000!")
            attempts -= 1  # Don't count out-of-range as an attempt
            continue

        if guess < secret_number:
            print(f"Too low! {remaining} attempts remaining.")
        elif guess > secret_number:
            print(f"Too high! {remaining} attempts remaining.")
        else:
            print("\n" + "*" * 50)
            print(f"Congratulations! You guessed it in {attempts} attempt(s)!")
            print("*" * 50)
            return True

    print("\n" + "-" * 50)
    print(f"Game Over! The number was {secret_number}.")
    print("-" * 50)
    return False


def main():
    """Main game loop."""
    print("\n" + "#" * 50)
    print("#" + " " * 14 + "NUMBER GUESSING GAME" + " " * 14 + "#")
    print("#" * 50)

    wins = 0
    games = 0

    while True:
        games += 1
        if play_game():
            wins += 1

        print(f"\nScore: {wins} wins out of {games} games")

        play_again = input("\nPlay again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("\nThanks for playing! Goodbye!\n")
            break


if __name__ == "__main__":
    main()
