class Settings:
    """A class to store all the settings for Hangman"""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Game settings
        self.max_guesses = 6
        self.right_history = []
        self.wrong_history = []
