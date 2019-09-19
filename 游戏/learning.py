import pygame, sys, math
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800,600))
back_color = 255, 255, 255
_color = 0, 0, 0

load_Image = pygame.image.load('C://Users//10248//Desktop//tex3.png').convert_alpha()
load_new_image = pygame.image.load('C://Users//10248//Desktop//t.jpg').convert_alpha()
load_dog_human = pygame.image.load('C://Users//10248//Desktop//timg.jpg').convert_alpha()
dog_x, dog_y = load_dog_human.get_size()
load_dog_human = pygame.transform.smoothscale(load_dog_human,(dog_x//2, dog_y//2))
image_x, image_y = load_Image.get_size()
angle = 0.0

while 1:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            pygame.quit()
            sys.exit()


    pos_x = math.sin(math.radians(angle))*200
    pos_y = math.cos(math.radians(angle))*200
    old_pos_x, old_pos_y = 0,0
    angle += 0.1
    delta_x = (pos_x - old_pos_x)
    delta_y = (pos_y - old_pos_y)
    rangle = math.atan2(delta_y, delta_x)
    rangled = (-math.degrees(rangle))%360
    new_load_dog_human = pygame.transform.rotate(load_dog_human, rangled)
    screen.fill(back_color)
    screen.blit(load_new_image,(0,0))
    screen.blit(load_Image, ((800-image_x)/2,(600-image_y)/2))
    width, height = new_load_dog_human.get_size()
    screen.blit(new_load_dog_human,(550+pos_x-image_x//2,360+pos_y-image_y//2))
    pygame.display.update()

    old_pos_x = pos_x
    old_pos_y = pos_y