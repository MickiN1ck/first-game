import pygame as pg
from player import Player


class Shot:
    def __init__(self, image: pg.Surface, x: int, y: int):
        self.picture = image
        self.speed = 5
        self.damage = 1
        self.body_rect = pg.rect.Rect(x, y,
                                      self.picture.get_width(), self.picture.get_height())

    def draw(self, screen: pg.Surface):
        screen.blit(self.picture, (self.body_rect.x, self.body_rect.y))

    def is_hit(self, player: Player):
        if player.body_rect.right >= self.body_rect.centerx >= player.body_rect.left \
                and player.body_rect.bottom >= self.body_rect.centery >= player.body_rect.top:
            player.get_damage(self.damage)
            return True
        else:
            return False

    def move(self):
        self.body_rect.x -= self.speed
