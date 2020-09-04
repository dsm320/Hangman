import pygame
import sys

import game_functions as gf

from settings import Settings


def run_game():
    # Initialize game, settings, screen
    pygame.init()
    settings = Settings()

    # Picks word
    word = gf.pick_word()
    # print(word)

    # Sets guess count
    guess_count = 0

    # Start main loop of the game
    while not gf.check_win(word, settings):
        display = ''

        for char in word:
            if char not in settings.right_history:
                display += '_ '
            elif char in settings.right_history:
                display += char + ' '

        print(display)
        print(settings.wrong_history)
        print("\n")

        char = input("Guess a character in the word: ")
        if not gf.check_guess(char, word, settings) and \
                char not in settings.right_history and \
                char not in settings.wrong_history:
            guess_count += 1
        if len(settings.wrong_history) >= settings.max_guesses:
            print("You lose. Guess count has been exceeded")
            break

    print("The word was '" + word + "'.")
    sys.exit()

run_game()
