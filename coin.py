import pygame as pg
from player import Player


class Coin:
    def __init__(self, image: pg.Surface, x: int, y: int, sound: pg.mixer.Sound):
        self.sound = sound
        self.sound.set_volume(0.4)
        self.picture = image
        self.body_rect = pg.rect.Rect(x, y,
                                      self.picture.get_width(), self.picture.get_height())

    def draw(self, screen: pg.Surface):
        screen.blit(self.picture, (self.body_rect.x, self.body_rect.y))

    def is_touch(self, player: Player):
        if player.body_rect.right >= self.body_rect.centerx >= player.body_rect.left \
                and player.body_rect.bottom >= self.body_rect.centery >= player.body_rect.top:
            return True
        else:
            return False
