import random

# Hangman Word Guessing Game
# Run: python hangman.py

WORDS = [
    "python", "computer", "internship", "programming", "developer",
    "keyboard", "database", "science", "project", "analytics",
    "function", "variable", "software", "student", "technology"
]

HANGMAN_STAGES = [
    # 0 wrong guesses
    r"""
     +---+
     |   |
         |
         |
         |
         |
    =========""",
    # 1 wrong guess
    r"""
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",
    # 2 wrong guesses
    r"""
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",
    # 3 wrong guesses
    r"""
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    # 4 wrong guesses
    r"""
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =========""",
    # 5 wrong guesses
    r"""
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =========""",
    # 6 wrong guesses: game over
    r"""
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    ========="""
]


def display_word(secret_word, correct_guesses):
    """Return the word with unguessed letters hidden."""
    return " ".join(letter.upper() if letter in correct_guesses else "_" for letter in secret_word)


def play_hangman():
    secret_word = random.choice(WORDS)
    correct_guesses = set()
    guessed_letters = set()
    wrong_guesses = 0
    max_attempts = 6

    print("=" * 38)
    print("       HANGMAN WORD GUESSING GAME")
    print("=" * 38)
    print(f"Guess the hidden word one letter at a time. You have {max_attempts} wrong guesses.")
    print("Enter one English letter per turn.\n")

    while wrong_guesses < max_attempts:
        print(HANGMAN_STAGES[wrong_guesses])
        print("\nWord:", display_word(secret_word, correct_guesses))
        print("Guessed letters:", " ".join(sorted(guessed_letters)) if guessed_letters else "None")
        print(f"Wrong guesses left: {max_attempts - wrong_guesses}")

        # Check for victory before asking for another letter.
        if all(letter in correct_guesses for letter in secret_word):
            print("\nCongratulations! You guessed the word!")
            print("Secret word:", secret_word.upper())
            print("YOU WIN!")
            return

        guess = input("\nEnter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha() or not guess.isascii():
            print("Invalid input. Please enter one English letter (A-Z).\n")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess.upper()}'. No attempt was lost.\n")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            correct_guesses.add(guess)
            print(f"Correct! '{guess.upper()}' is in the word.\n")
        else:
            wrong_guesses += 1
            print(f"Sorry, '{guess.upper()}' is not in the word.\n")

    print(HANGMAN_STAGES[max_attempts])
    print("\nYOU LOSE!")
    print("The secret word was:", secret_word.upper())


def main():
    while True:
        play_hangman()
        again = input("\nWould you like to play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing Hangman. Goodbye!")
            break
        print()


if __name__ == "__main__":
    main()
