import pygame as pg
from player import Player


class Platform:
    def __init__(self, image: str, x: int, y: int):
        self.pic = pg.image.load(f"картинки/{image}")
        self.shift_x = 15
        self.shift_y = 13
        self.body_rect = pg.rect.Rect(x + self.shift_x, y,
                                      self.pic.get_width() - self.shift_x * 2, self.pic.get_height() - 70)
        self.has_player = False

    def draw(self, screen: pg.Surface):
        screen.blit(self.pic, (self.body_rect.x - self.shift_x, self.body_rect.y - self.shift_y))
        # pg.draw.rect(screen, "red", self.body_rect, 2)

    def update(self, player: Player):
        # приземление на платформу
        if not player.is_jumping and self.is_touching(player) and not self.has_player:
            player.gravity_speed = 0
            player.grounded = True
            player.body_rect.bottom = self.body_rect.top
            self.has_player = True
        # сход с платформы
        elif self.has_player and not self.is_touching(player):
            player.grounded = False
            self.has_player = False

    def is_touching(self, player: Player):
        if (self.body_rect.bottom >= player.body_rect.bottom >= self.body_rect.top
                and player.body_rect.left <= self.body_rect.right
                and player.body_rect.right >= self.body_rect.left):
            return True
        else:
            return False
