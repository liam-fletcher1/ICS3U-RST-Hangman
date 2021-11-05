#!/usr/bin/env python3

# Created by: Liam Fletcher
# Created on: Nov 2021
# This program is the game "Hangman"

import random

word_list = [
    "dog",
    "cat",
    "pizza",
    "chicken",
    "coding",
    "python",
    "space",
    "class",
    "math",
]


def get_word(word_list):
    word = random.choice(word_list)
    return word.upper()


# Some info found from: https://www.youtube.com/watch?v=m4nEnsavl6w
def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    tries = 6
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Guess a letter (NO FULL WORDS): ").upper()

        # Some info found from: https://www.youtube.com/watch?v=5x6iAKdJB6U&t=470s
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already entered", guess, "!")

            elif guess not in word:
                print(guess, "isn't in the word.")
                tries -= 1
                guessed_letters.append(guess)

            # Some info found from: https://www.youtube.com/watch?v=3_CX0aD9Fdg
            else:
                print("Great job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]

                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)

                if "_" not in word_completion:
                    guessed = True

        else:
            print("invalid input")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    if guessed:
        print("Great job, you guessed the word!")
    else:
        print("You lose. The word was " + word + "!")


# Graphics info found from: shorturl.at/belG0
def display_hangman(tries):
    stages = [
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                   """,
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                   """,
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                   """,
        """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                   """,
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                   """,
        """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                   """,
        """
                   --------
                   |      |
                   |      
                   |
                   |
                   |
                   -
                   """,
    ]
    return stages[tries]


def main():
    word = get_word(word_list)
    play(word)
    while input("Again? (Y/N) ").upper() == "Y":
        word = get_word(word_list)
        play(word)


if __name__ == "__main__":
    main()
