import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    def __init__(self, ai_settings, screen):
        """初始化星星并设置其初始位置"""
        super(Star, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载星星图像，并设置其rect属性
        self.image0 = pygame.image.load('img/alien.png')
        self.image = pygame.transform.scale(self.image0, (100, 100))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 每个星星最初都在屏幕随机位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        """在指定位置绘制星星"""
        self.screen.blit(self.image, self.rect)
