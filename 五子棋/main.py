import pygame
import sys


class AI(object):
    def __init__(self):
        self.ai_mov = []

    def think_action(self, d):
        min_key = float("inf")
        pos = None
        ai_fill = []
        player_fill = []
        for i in d.check_board.keys():
            player_fill.extend(d.check_board.keys())
            player_fill.remove(i)
            player_fill.extend(d.player_mov)
            n1 = calculation(player_fill, d)
            ai_fill.extend(d.check_board.keys())
            n2 = calculation(ai_fill, d)
            if min_key > (n1 - n2):
                min_key = n1 - n2
                pos = i
            player_fill = []
            ai_fill = []
        self.ai_mov.append(pos)
        del d.check_board[pos]
        return pos


class Data(object):
    def __init__(self):
        self.check_board = {(0, 0): (0, 0, 200, 200),
                            (1, 0): (200, 0, 400, 200),
                            (2, 0): (400, 0, 600, 200),
                            (0, 1): (0, 200, 200, 400),
                            (1, 1): (200, 200, 400, 400),
                            (2, 1): (400, 200, 600, 400),
                            (0, 2): (0, 400, 200, 600),
                            (1, 2): (200, 400, 400, 600),
                            (2, 2): (400, 400, 600, 600)}
        self.BOARD = {(0, 0): (0, 0, 200, 200),
                      (1, 0): (200, 0, 400, 200),
                      (2, 0): (400, 0, 600, 200),
                      (0, 1): (0, 200, 200, 400),
                      (1, 1): (200, 200, 400, 400),
                      (2, 1): (400, 200, 600, 400),
                      (0, 2): (0, 400, 200, 600),
                      (1, 2): (200, 400, 400, 600),
                      (2, 2): (400, 400, 600, 600)}
        self.right = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)],
        ]
        self.player_mov = []


def check_chess(chess, d):
    for i in d.right:
        if set(i).issubset(chess):
            return True
    return False


def calculation(mov, d):
    num = 0
    for i in d.right:
        if set(i).issubset(set(mov)):
            num += 1
    return num


def main():
    a = AI()
    d = Data()
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    font_obj = pygame.font.Font(None, 80)
    screen.fill(color=(255, 255, 255))
    pygame.display.set_caption('井字棋')
    while True:
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    for k, v in d.check_board.items():
                        if v[0] <= x <= v[2] and v[1] <= y <= v[3]:
                            draw_circle(screen, ((v[0] + v[2]) // 2, (v[1] + v[3]) // 2,))
                            d.player_mov.append(k)
                            del d.check_board[k]
                            break
                    pos = a.think_action(d)
                    draw_x(screen, pos, d)
                    if check_chess(a.ai_mov, d):
                        text_image = font_obj.render('AI WIN!', True, (0, 0, 0))
                        screen.blit(text_image, (190, 300))
                    if check_chess(d.player_mov, d):
                        text_image = font_obj.render('PLAYER WIN!', True, (0, 0, 0))
                        screen.blit(text_image, (150, 300))
            draw_line(screen)
        except KeyError:
            text_image = font_obj.render('NO WINNER!', True, (0, 0, 0))
            screen.blit(text_image, (100, 300))
        pygame.display.update()


def draw_line(screen):
    pygame.draw.aaline(screen, (0, 0, 0), (0, 200), (600, 200))
    pygame.draw.aaline(screen, (0, 0, 0), (0, 400), (600, 400))
    pygame.draw.aaline(screen, (0, 0, 0), (200, 0), (200, 600))
    pygame.draw.aaline(screen, (0, 0, 0), (400, 0), (400, 600))


def draw_circle(screen, pos):
    pygame.draw.circle(screen, (0, 255, 0), pos, 100, 1)


def draw_x(screen, pos, d):
    start = d.BOARD[pos]
    pygame.draw.aaline(screen, (255, 0, 0), (start[0], start[1]), (start[0] + 200, start[1] + 200))
    pygame.draw.aaline(screen, (255, 0, 0), (start[0], start[1] + 200), (start[0] + 200, start[1]))


if __name__ == '__main__':
    main()
