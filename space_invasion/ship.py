import pygame

class Ship:
    """
    A class to imanage the ship.
    """

    def __init__(self, ai_game):
        """
        Construct the ship and setup starting position.
        """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Let's load the ship image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # Start each new ship at bottom
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flag
        self.moving_right = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right:
            self.rect.x += 1

    def blitme(self):
        """
        Draw the ship at its current location.
        """
        self.screen.blit(self.image, self.rect)

