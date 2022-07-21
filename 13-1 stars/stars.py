import sys
import pygame
from pygame.sprite import Sprite
from random import randint

class Star(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        self.image = pygame.image.load('star.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

class starsInSky:
    """Arrange stars randomly on screen"""
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200,800))
        self.stars = pygame.sprite.Group()

        self._create_starSky()

    def run_game(self):
        while True:
            self._update_screen()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def _update_screen(self):
        self.screen.fill((0, 102, 204))
        self.stars.draw(self.screen)
        pygame.display.flip()

    def _create_starSky(self):
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = 1200 - 2 * star_width
        number_star_x = available_space_x // star_width

        available_space_y = 800 - 2 * star_height
        number_rows = available_space_y // star_height

        for row_num in range(number_rows):
            for star_num in range(number_star_x):
                self._create_star(star_num, row_num)
    
    def _create_star(self, star_num, row_num):
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star_width * (star_num + randint(-3, 0))
        star.rect.x = star.x
        # star.rect.y = star_height + 2 * star_height * row_num + randint(-10, 10)
        star.rect.y = star.rect.height + 2 * star.rect.height * (row_num + randint(-5, 0))
        self.stars.add(star)



if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = starsInSky()
    ai.run_game()
