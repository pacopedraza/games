import sys
import pygame

class GameAlienInvasion:
    """
    Class to manage all the game assets and behavior,
    """

    def __init__(self):
        """
        First, we will initialize the game, then
        we will create game resources.
        """
        pygame.init()

        self.screen_conf = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

