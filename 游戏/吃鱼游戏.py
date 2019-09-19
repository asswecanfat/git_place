import pygame, sys, random
from pygame.locals import *
from datetime import datetime, date, time

def trans_image(image, big_num):
    new_image = pygame.image.load(image).convert_alpha()
    new_x, new_y = new_image.get_size()
    new_image = pygame.transform.smoothscale(new_image, (new_x//big_num, new_y//big_num))
    new_x, new_y = new_image.get_size()
    return new_image, new_x, new_y

pygame.init()
back_color = 0, 255, 255#
screen = pygame.display.set_mode((800,600))#
pygame.display.set_caption('Catch fish')#
lives_font = pygame.font.SysFont('dengxian',20)#
score_font = pygame.font.SysFont('dengxian',20)#
sure_me = pygame.font.SysFont('dengxian',20)#
title_font = pygame.font.SysFont('kaiti',120)#
play_font = pygame.font.SysFont('kaiti',50)#
round_font = pygame.font.SysFont('dengxian',20)#
ending_font = pygame.font.SysFont('方正粗黑宋简体',80)#
count = 0

kua_move_Image, kua_move_x, kua_move_y = trans_image('kua_move.jpg', 3)
kua_move_vel_x = 2

fish_Image, fish_x, fish_y = trans_image('kua_love.jpg',10)
fish_vel = 1
fish_now_y = -fish_y

sure_start = False
pos_x = (800-kua_move_x)/2
lives = 1
fish_now_x = random.randint(0,800-fish_x)
fish_count = 0
score = 0
WAIT = USEREVENT + 1
y_pass_long = 50
n = 1 #系数
lives_n = 10
health = 100
health_n = 1
sure_use = 1

def lives_fun(lives, fish_ver):
    if lives == 1:
        screen.blit(fish_Image, (fish_now_x,fish_ver - y_pass_long))
        return 1
    elif lives == 2:
        screen.blit(fish_Image, (fish_now_x, fish_ver-random.randint(0,lives)*y_pass_long))
        return 1
    return 0
def draw_ending(now_lives):
    screen.fill(back_color)
    ending_text = ending_font.render('游戏结束', 1, (0, 0, 0))
    weith, hight = ending_text.get_size()
    screen.blit(ending_text, ((800-weith)/2,(600-hight)/3))
    new_lives_text = lives_font.render('LIVES:' + str(now_lives),1,(0,0,0))
    screen.blit(new_lives_text, (0,0))
    score_text = score_font.render('SCORE:' + str(score), 1, (0, 0, 0))
    screen.blit(score_text, (800-score_text.get_size()[0], 0))
def lives_fish(now_lives, n):
    fish_num = now_lives*10*n
    return fish_num

def fish_x_sure(fish_x_now, fish_y_now,now_score,now_fish_count, now_health):

    return fish_x_now,fish_y_now,now_fish_count,now_score,now_health

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            if count == 0:
                mouse_x, mouse_y = event.pos
    screen.fill(back_color)
    lives_text1 = lives_font.render('TOTAL LIVES:10',1,(0,0,0))
    sure_text = sure_me.render('Copyright ©2019 developed by ass-boy',1,(0,0,0))
    title_text = title_font.render('抓鱼游戏', 1, (255,0,0))
    play_text = play_font.render('点击此处进行游玩', 1, (255,0,255))#(400, 51)
    screen.blit(lives_text1, (0,0))
    screen.blit(sure_text,(460,570))
    screen.blit(title_text,(180,150))
    screen.blit(play_text,(210,350))

    try:
        if 210 <= mouse_x <= 610 and 350 <= mouse_y <= 401:
            count += 1
            screen.fill(back_color)
            lives_text = lives_font.render('TOTAL LIVES:10', 1, (0, 0, 0))
            screen.blit(lives_text, (0, 0))
            round_text = round_font.render('LIVES:'+str(lives-1), 1, (0, 0, 0))
            screen.blit(round_text, ((800-round_text.get_size()[0])/2, 0))
            score_text = score_font.render('SCORE:'+ str(score), 1, (0, 0, 0))
            screen.blit(score_text, (800-score_text.get_size()[0], 0))
            if count and health > 0 and sure_use:
                screen.blit(kua_move_Image, (pos_x,600-kua_move_y))
                if fish_count < lives_fish(lives,n):
                    sure_use = lives_fun(lives, fish_now_y)
                    fish_now_y += (fish_vel + (lives-1)*1.2)
                    if pos_x <= fish_now_x <= pos_x + kua_move_x:
                        if 600 - kua_move_y <= fish_now_y < 600:  # if fish_now_y >= 600-kua_move_y:
                            score += 100
                            fish_now_x = random.randint(0, 800 - fish_x)
                            fish_now_y = -fish_y - y_pass_long * n
                            fish_count += 1
                    else:
                        if fish_now_y >= 600:
                            fish_now_x = random.randint(0, 800 - fish_x)
                            fish_now_y = -fish_y - y_pass_long * n
                            fish_count += 1
                            health -= 5 * 0  # health_n
                else:
                    lives += 1
                    fish_count = 0
                    n -= 0.2
            else:
                draw_ending(lives)
            keys = pygame.key.get_pressed()
            if keys[K_LEFT] or keys[K_a]:
                pos_x -=  kua_move_vel_x
            elif keys[K_RIGHT] or keys[K_d]:
                pos_x +=  kua_move_vel_x
            if pos_x < 0:
                pos_x = 0
            elif pos_x > 800-kua_move_x:
                pos_x = 800-kua_move_x

    except:
        pass
    pygame.display.update()

