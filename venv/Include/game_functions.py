import pygame
import sys

from random import randint

from settings import Settings


def check_events():
    """Responds to key presses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def pick_word():
    """Randomly generates the word to be guessed"""
    word_list = []
    # Read in potential words
    with open('common_words.txt') as dic_file:
        words = dic_file.readlines()
        for word in words:
            if len(word) >= 5:
                word_list.append(word.strip())

    return word_list[randint(1, len(word_list))]

def check_guess(char, word, settings):
    """Checks to see if guessed letter is contained in the chosen word"""
    if char not in settings.right_history and \
            char not in settings.wrong_history and \
            len(char) == 1:
        if char in word:
            settings.right_history.append(char)
            return True
        elif char not in word:
            settings.wrong_history.append(char)
            return False
        elif len(char) > 1:
            print("You cannot enter more than one character per guess.")

def check_win(word, settings):
    """Check to see if game is won"""
    for char in word:
        if char not in settings.right_history:
            return False
    print("Congratulations! You have won!")
    return True
