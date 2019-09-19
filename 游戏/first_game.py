import pygame, sys, math
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((500,500))
back_color = 255,255,255
_color = 0,0,0

def draw_1(color,x,y,big):
    start_angle = math.radians(290)
    end_angle = math.radians(340)
    pygame.draw.arc(screen,color,(x,y,big[0],big[1]),start_angle,end_angle)
    pygame.draw.line(screen,color,(x + big[0]*0.97,y + big[1]*0.69),(x + big[0]*0.97,y + big[1]*1.5))
    pygame.draw.line(screen,color,(x + big[0]*0.97,y + big[1]*1.5),(x + big[0]*0.67,y + big[1]*1.5))
    pygame.draw.line(screen, color, (x + big[0]*0.97, y + big[1]*1.5), (x + big[0]*1.27, y + big[1]*1.5))

def draw_2(color,x,y,big):
    start_angle = math.radians(0)
    end_angle = math.radians(180)
    pygame.draw.arc(screen,color,(x,y,big[0],big[1]),start_angle,end_angle)
    pygame.draw.line(screen,color,(x + big[0],y + big[1]/2),(x + big[0]/10,y + big[1]*2))
    pygame.draw.line(screen,color,(x + big[0]/10,y + big[1]*2),(x + big[0]/10+big[0],y + big[1]*2))

def draw_3(color,x,y,big):
    start_angle = math.radians(270)
    end_angle = math.radians(90)
    pygame.draw.arc(screen, color, (x, y, big[0], big[1]), start_angle, end_angle)
    pygame.draw.arc(screen, color, (x, y + big[1], big[0], big[1]), start_angle, end_angle)

def draw_4(color,x,y,big = 1):
    pygame.draw.line(screen,color,(x,y),(x + 10*big, y - 20*big))
    pygame.draw.line(screen,color,(x, y),(x + 23*big, y))
    pygame.draw.line(screen,color,(x + 10*big + 10, y - 20*big), (x + 10*big + 10, y - (-10)*big))

sure_1 = False
sure_2 = False
sure_3 = False
sure_4 = False
start_angle1, end_angle1 = math.radians(90), math.radians(180)
start_angle2, end_angle2 = math.radians(0), math.radians(90)
start_angle3, end_angle3 = math.radians(180), math.radians(270)
start_angle4, end_angle4 = math.radians(270), math.radians(360)
count = 1
myfont = pygame.font.Font(None,60)
sure_mouse_x = False
sure_mouse_y = False
end_font = pygame.font.Font(None,40)

while 1:
    for event in pygame.event.get():
        if event.type is QUIT:
            sys.exit()
        elif event.type == KEYUP:
            if event.key == pygame.K_SPACE:
                count = 0
                sure_mouse_x = False
                sure_mouse_y = False
                sys.exit()
            elif event.key == pygame.K_1:
                sure_1 = True
            elif event.key == pygame.K_2:
                sure_2 = True
            elif event.key == pygame.K_3:
                sure_3 = True
            elif event.key == pygame.K_4:
                sure_4 = True
        elif event.type == MOUSEBUTTONDOWN:
            mouse_x,mouse_y = event.pos
            if 200 <= mouse_x <= 260:
                sure_mouse_x = True
            if 250 <= mouse_y <= 310:
                sure_mouse_y = True
    if count:
        screen.fill(back_color)
        textImage = myfont.render('PLAY',True,_color)
        screen.blit(textImage,(200,250))
        if sure_mouse_y and sure_mouse_x:
            count = 0
            sure_mouse_x = False
            sure_mouse_y = False
    else:
        screen.fill(back_color)
        #pygame.draw.arc(screen,_color,(50,50,400,400),math.radians(0),math.radians(360))
        pygame.draw.line(screen,_color,(0,250),(500,250))
        pygame.draw.line(screen,_color,(250,0),(250,500))
        draw_1(_color,80,80,(100,100))
        draw_2(_color,300,100,(60,60))
        draw_3(_color,120,280,(60,60))
        draw_4(_color,300,350,3)
        if sure_1:
            pygame.draw.arc(screen,(255,0,0),(50,50,400,400),start_angle1,end_angle1)
        if sure_2:
            pygame.draw.arc(screen, (255, 0, 0), (50, 50, 400, 400), start_angle2, end_angle2)
        if sure_3:
            pygame.draw.arc(screen,(255,0,0),(50,50,400,400),start_angle3,end_angle3)
        if sure_4:
            pygame.draw.arc(screen,(255,0,0),(50,50,400,400),start_angle4,end_angle4)
        if sure_1 and sure_2 and sure_3 and sure_4:
            back_color = 0,255,255
            screen.fill(back_color)
            end_textImage = end_font.render('Thanks for playing this Demo!!',True,_color)
            screen.blit(end_textImage,(50,250))
    pygame.display.update()