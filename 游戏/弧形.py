import pygame
from pygame.locals import *
import math
import sys

pygame.init()
screen = pygame.display.set_mode((500,500))
back_color = 255,255,255
start_angle = math.radians(90)
end_angle = math.radians(360)
hu_color = 0,0,0
rect = 150,250,200,200

while 1:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            pygame.quit()
            sys.exit()

    screen.fill(back_color)
    pygame.draw.arc(screen,hu_color,rect,start_angle,end_angle,3)
    pygame.display.update()
