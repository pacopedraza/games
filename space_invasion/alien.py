"""
This class is going to manage the alien.
This class is very similar to the ship class,
changing only the position where we display the
alien.
"""
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent an alien"""

    def __init__(self, ai_game):
        """Init the alien and set the first position"""
        super().__init__()
        self.screen = ai_game.screen

        # Loads the alien image
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alient near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the horizontal position of the alien
        self.x = float(self.rect.x)
