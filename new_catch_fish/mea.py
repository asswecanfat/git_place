import pygame
import random
from pygame.sprite import Sprite


class Mea(Sprite):
    def __init__(self, screen, ai_settings):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('mea.jpg')
        self.mea_x, self.mea_y = self.image.get_size()
        self.image = pygame.transform.smoothscale(self.image,
                                                  (self.mea_x // ai_settings.mea_big,
                                                   self.mea_y // ai_settings.mea_big))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = random.randint(0, ai_settings.screen_width - self.rect.width), -self.rect.height
        self.vel = ai_settings.mea_fly_vel_y

    def update(self):
        self.rect.y += self.vel

    def draw_mea(self):
        self.screen.blit(self.image, self.rect)
