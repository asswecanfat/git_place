import pygame
import random
from pygame.sprite import Sprite


class Mushroom(Sprite):
    def __init__(self, screen, ai_settings):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('mushroom.jpg')
        self.mushroom_x, self.mushroom_y = self.image.get_size()
        self.image = pygame.transform.smoothscale(self.image,
                                                  (self.mushroom_x // ai_settings.mushroom_big,
                                                   self.mushroom_y // ai_settings.mushroom_big))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = random.randint(0, ai_settings.screen_width - self.rect.width), -self.rect.height
        self.vel = ai_settings.mushroom_fly_vel

    def update(self):
        self.rect.y += self.vel

    def draw_mushroom(self):
        self.screen.blit(self.image, self.rect)
