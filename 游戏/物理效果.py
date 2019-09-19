import pygame, sys, random
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600,600))
back_color = 255, 255, 255
_color = 0,0,0
rel_gality = 0.006
x = random.randint(0,500)
myfont = pygame.font.SysFont('SimHei',30)

def draw_ball(screen,color,x, y):
    return pygame.draw.rect(screen, color, (x, y, 100, 100))


while 1:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            rel_x, rel_y = pygame.mouse.get_rel()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos_x, pos_y = pygame.mouse.get_pos()

    screen.fill(back_color)
    try:
        reCt = draw_ball(screen, _color, pos_x, pos_y)
        if 0 <= pos_y < 500:
            pos_x = pos_x
            pos_y += rel_gality*pos_y
            pass
        else:
            pos_y = 500
            
    except:
        pass
    text = myfont.render('请点击鼠标左键生成小正方形',1, _color)
    screen.blit(text,(0,0))

    pygame.display.update()

