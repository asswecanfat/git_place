import pygame
from pygame.sprite import Sprite


class Kua(Sprite):
    def __init__(self, screen, ai_settings):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('kua_move.jpg')
        self.kua_x, self.kua_y = self.image.get_size()
        self.image = pygame.transform.smoothscale(
            self.image,
            (self.kua_x//ai_settings.kua_big,
             self.kua_y//ai_settings.kua_big))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = \
            (ai_settings.screen_width - self.rect.width)/2,\
            ai_settings.screen_hight - self.rect.height

    def update(self, ai_settings):
        if ai_settings.kua_move_eat is False and ai_settings.kua_move_miss is False:
            self.image = pygame.image.load('kua_move.jpg')
            self.kua_x, self.kua_y = self.image.get_size()
            self.image = pygame.transform.smoothscale(self.image,
                                                      (self.kua_x // ai_settings.kua_big,
                                                       self.kua_y // ai_settings.kua_big))
        if ai_settings.kua_move_eat:
            self.image = pygame.image.load('kua_success.jpg')
            self.kua_x, self.kua_y = self.image.get_size()
            self.image = pygame.transform.smoothscale(self.image,
                                                      (self.kua_x // ai_settings.kua_big,
                                                       self.kua_y // ai_settings.kua_big))
        if ai_settings.kua_move_miss:
            self.image = pygame.image.load('kua_fail.jpg')
            self.kua_x, self.kua_y = self.image.get_size()
            self.image = pygame.transform.smoothscale(self.image,
                                                      (self.kua_x // ai_settings.kua_big,
                                                       self.kua_y // ai_settings.kua_big))
        if ai_settings.kua_move_left_sure:
            self.rect.x -= ai_settings.kua_move_vel_x
        if ai_settings.kua_move_right_sure:
            self.rect.x += ai_settings.kua_move_vel_x
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > ai_settings.screen_width - self.rect.width:
            self.rect.x = ai_settings.screen_width - self.rect.width

    def draw_kua(self):

        self.screen.blit(self.image, self.rect)
