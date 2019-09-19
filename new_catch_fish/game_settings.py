import pygame
from pygame.sprite import Group


class Settings:
    def __init__(self):
        self.screen_width = 800
        self.screen_hight = 600
        self.bg_color = (0, 255, 255)
        # 字体
        self.lives_font = pygame.font.SysFont('dengxian', 20)
        self.score_font = pygame.font.SysFont('dengxian', 20)
        self.sure_me = pygame.font.SysFont('dengxian', 20)
        self.title_font = pygame.font.SysFont('kaiti', 120)
        self.play_font = pygame.font.SysFont('kaiti', 50)
        self.round_font = pygame.font.SysFont('dengxian', 20)
        self.ending_font = pygame.font.SysFont('方正粗黑宋简体', 80)
        self.re_start_font = pygame.font.SysFont('方正粗黑宋简体', 60)
        # 内容
        self.lives_text = 'TOTAL LIVES:3'
        self.score_text = 'SCORE:'
        self.sure_text = 'Copyright ©2019 developed by ass-boy'
        self.title_text = '抓鱼游戏'
        self.play_text = '点击此处进行游玩'
        self.round_text = 'LIVES:'
        self.ending_text = '游戏结束'
        self.re_start_text = '点此重新开始'
        # 分数
        self.score = 0
        # 啊夸行走速度
        self.kua_move_vel_x = 7
        # mea飞行速度
        self.mea_fly_vel_y = 2
        # mushroom的速度
        self.mushroom_fly_vel = 2
        # 鼠标位置
        self.mouse_x, self.mouse_y = 0, 0
        # 玩家血量
        self.health = 100
        # 游戏开始确认
        self.game_begin = 0
        # 游戏重新开始确认
        self.game_re_start = 0
        # kua图像大小
        self.kua_big = 3
        # mea图像大小
        self.mea_big = 8
        # mushroom的大小
        self.mushroom_big = 6
        # lives数
        self.lives = 1
        # kua_time图片显示次数
        self.kua_time_count = 0
        # 每个mea_miss的伤害
        self.mea_damge = 1
        # 每个mushroom的伤害
        self.mushroom_damge = 20
        # fps
        self.fps = 144
        # kua_move
        self.kua_move_left_sure = False
        self.kua_move_right_sure = False
        # kua_move状态
        self.kua_move_eat = False
        self.kua_move_miss = False
        # 间隔选择
        self.room_choices = [i for i in range(101) if i % 10 == 0]
        # kua,mea,mushroom初始化
        self.meas = Group()
        self.kua = Group()
        self.mushrooms = Group()
