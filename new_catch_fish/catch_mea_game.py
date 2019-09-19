import pygame
from game_settings import Settings
import game_fun as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_hight))
    gf.creat_mea(screen, ai_settings, ai_settings.meas)
    gf.creat_kua(screen, ai_settings, ai_settings.kua)
    gf.creat_mushroom(screen, ai_settings, ai_settings.mushrooms)
    clock = pygame.time.Clock()

    while 1:
        gf.check_event(ai_settings)
        gf.running(screen, ai_settings, ai_settings.kua, ai_settings.meas, ai_settings.mushrooms)
        gf.update_kua_meas_mushrooms(ai_settings.meas, ai_settings.mushrooms, ai_settings.kua, ai_settings)
        gf.update_mea(screen, ai_settings.meas, ai_settings)
        gf.update_kua(ai_settings.kua, ai_settings, screen)
        gf.update_mushroom(screen, ai_settings.mushrooms, ai_settings)
        gf.check_score(ai_settings)
        pygame.display.update()

        clock.tick(ai_settings.fps)


run_game()
