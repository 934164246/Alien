import pygame
from pygame.sprite import Group

import game_function as gf
from alien import Alien
from button import Button
from game_stats import GameStats
from scorebroad import Scoreboard
from settings import Settings
from ship import Ship
from star import Star


def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    # 创建存储游戏统计信息的实例，并创建记分牌
    sb = Scoreboard(ai_settings, screen, stats)

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    al_bullets = Group()
    # 创建一个用于存储外星人的编组
    aliens = Group()

    # 创建一个随机位置的星星
    star = Star(ai_settings, screen)

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 创建一个外星人
    alien = Alien(ai_settings, screen)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
                        aliens, bullets, star)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                              bullets, al_bullets, alien)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
                             bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button, al_bullets)


run_game()
