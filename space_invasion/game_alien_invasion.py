import sys
import pygame
from alien import Alien
from bullet import Bullet
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

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def launch_game(self):
        """
        This function will be the loop for the game.
        """
        while True:
            self._check_events()
            # Ship position will be updated after we've checked for
            # keyboard events and before we updated the screen.
            self.ship.update()
            self._update_bullets()
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
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q: # Quit when player press Q
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        """
        Update images on the screen, and flip to the new screen.
        """
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        pygame.display.flip() # Display the screen

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet position.
        # Below we will control to get rid of the bullets that have
        # Dissapear.
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets))

    def _create_fleet(self):
        """Create the fleet of our enemies (aliens)"""
        # Let's make our alien :)
        alien = Alien(self)
        alien_width = alien.rect.width
        # We need an empty margin on either side of the screen.
        # We will make this marginthe width of one alien.
        # Because we have two margins, the available space for aliens in
        # The screen width minus two aliens widths.
        available_space_x = self.settings.screen_width - (2 * alien_width)
        # We use floor division (//), wich divides two numbers and drops any
        # remainder, so we'll get an integer number of aliens.
        number_aliens_x = available_space_x // (2 * alien_width)

        # Create the first row of the aliens.
        for alien_number in range(number_aliens_x):
            # Create an alien and place it in the damn row.
            alien = Alien(self)
            alien.x = alien_width + 2 * alien_width * alien_number
            alien.rect.x = alien.x
            self.aliens.add(alien)


if __name__ == '__main__':
    # Creating game instance, then run the game
    obj_ai = GameAlienInvasion()
    obj_ai.launch_game()
