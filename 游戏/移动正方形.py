import pygame
from pygame.locals import *
import sys, time

pygame.init()
screen = pygame.display.set_mode((500,500))

re_x = 150
re_y = 200
v_x = 1
v_y = 1

while 1:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            pygame.quit()
            sys.exit()

    screen.fill((255,255,255))
    pygame.draw.rect(screen,(225,225,0),(re_x,re_y,100,100))

    re_x += v_x
    re_y += v_y

    if re_x > 400 or re_x < 0:
        v_x = -v_x
    if re_y > 400 or re_y < 0:
        v_y = -v_y
    time.sleep(0.001)
    pygame.display.update()


