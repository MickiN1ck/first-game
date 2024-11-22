import pygame as pg
from platform import Platform
from turret import Turret
from player import Player
from coin import Coin


class Location:
    def __init__(self, background: str, path: str, platforms: list[Platform], turrets: list[Turret], coins: list[Coin]):
        self.background = pg.image.load(f"картинки/{background}")
        self.path = pg.image.load(f"картинки/{path}")
        self.platforms = platforms
        self.turrets = turrets
        self.coins = coins

    def draw(self, screen: pg.Surface):
        screen.blit(self.background, (0, 0))
        screen.blit(self.path, (0, 680))
        for platform in self.platforms:
            platform.draw(screen)
        for turret in self.turrets:
            turret.draw(screen)
        for coin in self.coins:
            coin.draw(screen)

    def update(self, player: Player):
        for platform in self.platforms:
            platform.update(player)
        for turret in self.turrets:
            turret.update(player)
        for coin in self.coins:
            if coin.is_touch(player):
                self.coins.remove(coin)
                coin.sound.play()