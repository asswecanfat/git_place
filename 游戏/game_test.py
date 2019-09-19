import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))

myfont = pygame.font.SysFont('方正粗黑宋简体', 60)
white = 255, 255, 255
blue = 0, 0, 200

# 第一个参数是文本，第二个参数是抗锯齿字体，第三个参数是一个颜色值（RGB值）
textImage = myfont.render('Hello,pygame', True, white)
while 1:
    screen.fill(blue)
    screen.blit(textImage, (100, 100))
    for event in pygame.event.get():
        if event.type in (pygame.QUIT, pygame.KEYDOWN):
            pygame.quit()
            break

    position = 400, 400
    pygame.draw.circle(screen, white, position, 100, 100)
    pygame.display.update()

