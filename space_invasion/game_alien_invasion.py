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
            self._check_events()
            # Ship position will be updated after we've checked for
            # keyboard events and before we updated the screen.
            self.ship.update()
            self._update_screen()
            # Draw again the screen during each pass through the loop.

    def _check_events(self):
        """
        Respond to keypresses and mouse events.
        """
        for event in pygame.event.get(): # Mouse and keyboard events
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        """
        Update images on the screen, and flip to the new screen.
        """
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip() # Display the screen

if __name__ == '__main__':
    # Creating game instance, then run the game
    obj_ai = GameAlienInvasion()
    obj_ai.launch_game()
