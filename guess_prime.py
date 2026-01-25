"""Guess the Prime Number Game

A game where the player tries to guess a randomly selected prime number between 1 and 1000.
"""

import random


def is_prime(n):
    """Check if a number is prime.

    Args:
        n: Integer to check for primality.

    Returns:
        True if n is prime, False otherwise.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def generate_primes(start, end):
    """Generate all prime numbers in a given range.

    Args:
        start: Start of range (inclusive).
        end: End of range (inclusive).

    Returns:
        List of prime numbers in the range.
    """
    return [n for n in range(start, end + 1) if is_prime(n)]


def main():
    """Main game function."""
    print("=" * 50)
    print("    Welcome to Guess the Prime Number!")
    print("=" * 50)
    print("\nI'm thinking of a prime number between 1 and 1000.")
    print("Can you guess what it is?\n")

    # Generate all primes between 1 and 1000
    primes = generate_primes(1, 1000)

    # Randomly select one prime as the target
    target = random.choice(primes)

    attempts = 0

    # Game loop
    while True:
        user_input = input("Enter your guess: ")

        # Input handling with try-except
        try:
            guess = int(user_input)
        except ValueError:
            print("Invalid input! Please enter a valid integer.\n")
            continue

        attempts += 1

        # Check if input is within valid range
        if guess < 1 or guess > 1000:
            print("Please enter a number between 1 and 1000.\n")
            continue

        # Check if the guess is a prime number
        if not is_prime(guess):
            print(f"Hint: {guess} is not a prime number. Try a prime!\n")
            continue

        # Compare guess with target
        if guess < target:
            print("Too low! Try a higher prime number.\n")
        elif guess > target:
            print("Too high! Try a lower prime number.\n")
        else:
            # Correct guess - break the loop
            print(f"\nCongratulations! You guessed it!")
            print(f"The prime number was {target}.")
            print(f"It took you {attempts} attempt(s).")
            break

    print("\nThanks for playing!")


if __name__ == "__main__":
    main()
