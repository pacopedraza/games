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

        self.screen_conf = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Alien Invasion")

    def launch_game(self):
        """
        This function will be the loop for the game.
        """
        while True:
            for event in pygame.event.get(): # Mouse and keyboard events
                if event.type == pygame.QUIT:
                    sys.exit()

                pygame.display.flip() # Display the screen

if __name__ == '__main__':
    # Creating game instance, then run the game
    obj_ai = GameAlienInvasion()
    obj_ai.launch_game()
