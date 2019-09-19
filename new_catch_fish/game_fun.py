import pygame
import sys
import random
from mea import Mea
from kua import Kua
from mushroom import Mushroom


def display_begin_ui(screen, ai_settings):
    screen.fill(ai_settings.bg_color)
    pygame.display.set_caption('Catch fish')
    lives_text = ai_settings.lives_font.render(ai_settings.lives_text, 1, (0, 0, 0))
    screen.blit(lives_text, (0, 0))
    score_text = ai_settings.score_font.render(ai_settings.score_text + str(ai_settings.score), 1, (0, 0, 0))
    screen.blit(score_text, (screen.get_size()[0]-score_text.get_size()[0], 0))
    sure_text = ai_settings.sure_me.render(ai_settings.sure_text, 1, (0, 0, 0))
    screen.blit(sure_text, (screen.get_size()[0] - sure_text.get_size()[0],
                            screen.get_size()[1]-sure_text.get_size()[1]))
    title_text = ai_settings.title_font.render(ai_settings.title_text, 1, (255, 0, 0))
    screen.blit(title_text,
                ((screen.get_size()[0] - title_text.get_size()[0])/2,
                 (screen.get_size()[1] - title_text.get_size()[1])/3))
    play_text = ai_settings.play_font.render(ai_settings.play_text, 1, (255, 0, 255))
    screen.blit(play_text,
                ((screen.get_size()[0] - play_text.get_size()[0])/2,
                 (screen.get_size()[1] - title_text.get_size()[1])/1.3))
    return play_text.get_size()


def check_event(ai_settings):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if ai_settings.game_begin == 0:
                ai_settings.mouse_x, ai_settings.mouse_y = event.pos
            elif ai_settings.game_re_start == 0:
                ai_settings.mouse_x, ai_settings.mouse_y = event.pos
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                ai_settings.kua_move_left_sure = True
                ai_settings.kua_move_right_sure = False
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                ai_settings.kua_move_left_sure = False
                ai_settings.kua_move_right_sure = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                ai_settings.kua_move_left_sure = False
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                ai_settings.kua_move_right_sure = False


def mouse_sure_click_strat(screen, ai_settings, mouse_x, mouse_y, _strat):
    try:
        x_left_limit = (ai_settings.screen_width - _strat[0])/2
        x_right_limit = (ai_settings.screen_width + _strat[0])/2
        y_up_limit = (ai_settings.screen_hight - 2.3*_strat[1])/1.3
        y_down_limit = (ai_settings.screen_hight - _strat[1])/1.3
        if x_left_limit <= mouse_x <= x_right_limit and y_up_limit <= mouse_y <= y_down_limit:
            ai_settings.game_begin = 1
            screen.fill(ai_settings.bg_color)
    except pygame.error:
        pass


def mouse_sure_click_re_start(ai_settings, mouse_x, mouse_y, _re_strat):
    try:
        x_left_limit = (ai_settings.screen_width - _re_strat[0]) / 2
        x_right_limit = (ai_settings.screen_width + _re_strat[0]) / 2
        y_up_limit = ai_settings.screen_hight - _re_strat[1]
        y_down_limit = ai_settings.screen_hight
        if x_left_limit <= mouse_x <= x_right_limit and y_up_limit <= mouse_y <= y_down_limit:
            ai_settings.game_re_start = 1
    except pygame.error:
        pass


def display_game_ui(screen, ai_settings):
    screen.fill(ai_settings.bg_color)

    lives_text = ai_settings.lives_font.render(ai_settings.lives_text, 1, (0, 0, 0))
    screen.blit(lives_text, (0, 0))

    round_text = ai_settings.round_font.render(ai_settings.round_text + str(ai_settings.lives), 1, (0, 0, 0))
    round_text_width = round_text.get_size()[0]
    screen.blit(round_text, ((ai_settings.screen_width-round_text_width)/2, 0))

    score_text = ai_settings.score_font.render(ai_settings.score_text + str(ai_settings.score), 1, (0, 0, 0))
    screen.blit(score_text, (screen.get_size()[0] - score_text.get_size()[0], 0))


def display_ending_ui(screen, ai_settings):
    screen.fill(ai_settings.bg_color)
    ending_text = ai_settings.ending_font.render(ai_settings.ending_text, 1, (0, 0, 0))
    weith, hight = ending_text.get_size()
    screen.blit(ending_text, ((screen.get_size()[0] - weith) / 2,
                              (screen.get_size()[1] - hight) / 3))
    score_text = ai_settings.score_font.render(ai_settings.score_text + str(ai_settings.score), 1, (0, 0, 0))
    screen.blit(score_text, ((screen.get_size()[0] - score_text.get_size()[0])/2,
                             (screen.get_size()[1] - score_text.get_size()[1])/1.5))
    re_start_text = ai_settings.re_start_font.render(ai_settings.re_start_text, 1, (255, 0, 0))
    screen.blit(
        re_start_text,
        ((screen.get_size()[0] - re_start_text.get_size()[0]) / 2,
         (screen.get_size()[1] - re_start_text.get_size()[1])))
    return re_start_text.get_size()


def running(screen, ai_settings, kua, meas, mushrooms):
    if not ai_settings.game_begin:
        _strat = display_begin_ui(screen, ai_settings)
        mouse_sure_click_strat(screen, ai_settings, ai_settings.mouse_x,
                               ai_settings.mouse_y, _strat)
    elif ai_settings.game_begin and ai_settings.health > 0:
        display_game_ui(screen, ai_settings)
        kua.draw(screen)
        meas.draw(screen)
        mushrooms.draw(screen)
    elif ai_settings.game_begin and ai_settings.health <= 0:
        for i in kua:
            kua.remove(i)
        for _i in meas:
            meas.remove(_i)
        for _a in mushrooms:
            mushrooms.remove(_a)
        _re_start = display_ending_ui(screen, ai_settings)
        ai_settings.game_begin = -1
        mouse_sure_click_re_start(ai_settings, ai_settings.mouse_x, ai_settings.mouse_y, _re_start)
        if ai_settings.game_re_start:
            ai_settings.__init__()
            ai_settings.game_begin = 1


def creat_mea(screen, ai_settings, meas):
    if ai_settings.lives == 1:
        mea = Mea(screen, ai_settings)
        meas.add(mea)
        return len(meas)
    elif ai_settings.lives == 2:
        if len(meas) <= ai_settings.lives:
            random_num = random.sample(ai_settings.room_choices, ai_settings.lives)
            for i in range(len(meas), ai_settings.lives):
                mea = Mea(screen, ai_settings)
                mea.rect.y -= random_num[i]
                meas.add(mea)
        return len(meas)
    elif ai_settings.lives == 3:
        if len(meas) <= ai_settings.lives:
            random_num = random.sample(ai_settings.room_choices, ai_settings.lives)
            for i in range(len(meas), ai_settings.lives):
                mea = Mea(screen, ai_settings)
                mea.rect.y -= random_num[i]
                meas.add(mea)
        return len(meas)


def creat_kua(screen, ai_settings, kua):
    if len(kua) < 1:
        kua_s = Kua(screen, ai_settings)
        kua.add(kua_s)


def creat_mushroom(screen, ai_settings, mushrooms):
    if ai_settings.lives == 2:
        random_num = random.choice(ai_settings.room_choices)
        mushroom = Mushroom(screen, ai_settings)
        mushroom.rect.y -= random_num
        mushrooms.add(mushroom)
    elif ai_settings.lives == 3:
        random_num = random.sample(ai_settings.room_choices, ai_settings.lives)
        for i in range(len(mushrooms), ai_settings.lives - 1):
            mushroom = Mea(screen, ai_settings)
            mushroom.rect.y -= random_num[i]
            mushrooms.add(mushroom)
    return len(mushrooms)


def count_time(ai_settings):
    if ai_settings.kua_time_count < 200:
        ai_settings.kua_time_count += 1
    else:
        ai_settings.kua_move_eat = False
        ai_settings.kua_move_miss = False
        ai_settings.kua_time_count = 0


def check_score(ai_settings):
    if 0 <= ai_settings.score <= 1000:
        ai_settings.lives = 1
    elif 1000 < ai_settings.score <= 10000:
        ai_settings.lives = 2
    elif 10000 < ai_settings.score:
        ai_settings.lives = 3
        ai_settings.mea_fly_vel_y += ai_settings.lives*0.0005


def update_mea(screen, meas, ai_settings):
    if ai_settings.game_begin:
        count_time(ai_settings)
        meas.update()
        if len(meas) == ai_settings.lives:
            for i in meas.copy():
                if i.rect.y > ai_settings.screen_hight:
                    ai_settings.health -= ai_settings.mea_damge
                    ai_settings.kua_move_miss = True
                    ai_settings.kua_move_eat = False
                    meas.remove(i)
        elif len(meas) < ai_settings.lives:
            creat_mea(screen, ai_settings, meas)


def update_kua(kua, ai_settings, screen):
    if ai_settings.game_begin:
        if len(kua) < 1:
            creat_kua(screen, ai_settings, kua)
        else:
            kua.update(ai_settings)


def update_mushroom(screen, mushrooms, ai_settings):
    if ai_settings.game_begin and ai_settings.lives == 2:
        count_time(ai_settings)
        mushrooms.update()
        if len(mushrooms) == ai_settings.lives - 1:
            for i in mushrooms.copy():
                if i.rect.y > ai_settings.screen_hight:
                    ai_settings.health -= ai_settings.mushroom_damge
                    ai_settings.kua_move_miss = True
                    ai_settings.kua_move_eat = False
                    mushrooms.remove(i)
        elif len(mushrooms) < ai_settings.lives - 1:
            creat_mushroom(screen, ai_settings, mushrooms)


def update_kua_meas_mushrooms(meas, mushrooms, kua, ai_settings):
    collisions = pygame.sprite.groupcollide(meas, kua, True, False)
    _collisions = pygame.sprite.groupcollide(mushrooms, kua, True, False)
    if len(collisions) != 0:
        ai_settings.score += 100
        ai_settings.kua_move_miss = False
        ai_settings.kua_move_eat = True
    if len(_collisions) != 0:
        ai_settings.health -= ai_settings.mushroom_damge
        ai_settings.kua_move_miss = True
        ai_settings.kua_move_eat = False
