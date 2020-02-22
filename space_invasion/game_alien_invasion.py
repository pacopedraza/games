import sys
import pygame

from settings import Settings
from ship import Ship

class GameAlienInvasion:
    """
    Class to manage all the game assets and behavior.
    """

    def __init__(self):
        """
        First, we will initialize the game, then
        we will create game resources.
        """
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def launch_game(self):
        """
        This function will be the loop for the game.
        """
        while True:
            for event in pygame.event.get(): # Mouse and keyboard events
                if event.type == pygame.QUIT:
                    sys.exit()

                # Draw again the screen durin each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            pygame.display.flip() # Display the screen

if __name__ == '__main__':
    # Creating game instance, then run the game
    obj_ai = GameAlienInvasion()
    obj_ai.launch_game()
