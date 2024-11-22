import pygame as pg
from location import Location
from player import Player
from platform import Platform
from turret import Turret
from coin import Coin


class Game:
    def __init__(self):
        # фоновая музыка
        pg.mixer.init()
        pg.mixer.music.load("звуки/Dark Jungle Music - Aztec Temple.mp3")
        pg.mixer.music.set_volume(0.3)
        pg.mixer.music.play()
        self.width = 1550
        self.height = 810
        self.screen = pg.display.set_mode((self.width, self.height))
        coin_image = pg.image.load(f"картинки/монетка.png")
        coin_sound = pg.mixer.Sound("звуки/звук монетки.mp3")
        shot_sound = pg.mixer.Sound("звуки/звук выстрела.mp3")
        self.locations = [
            Location("джунгли.jpg", "дорожка 2 (1).png",
                     [Platform("платформа.png", 300, 500),
                      Platform("платформа.png", 100, 300),
                      Platform("платформа.png", 600, 200)],
                     [Turret("турель.png", 890, 78, "пуля.png", shot_sound)],
                     [Coin(coin_image, 500, 430, coin_sound),
                      Coin(coin_image, 310, 230, coin_sound),
                      Coin(coin_image, 1000, 670, coin_sound)]),


            Location("зимний лес.jpg", "дорожка 2 (1).png", [], [], [])
        ]
        self.current_location = self.locations[0]
        self.player = Player("чувачок.png", 50, 500)
        self.clock = pg.time.Clock()
        self.fps = 60
        self.heart = pg.image.load(f"картинки/сердечко.png")
        self.heart = pg.transform.scale(self.heart, (50, 50))

    def mainloop(self):
        while True:
            # тик часов
            self.clock.tick(self.fps)
            # передвижение персонажа
            self.player.update()
            # обновление локации
            self.current_location.update(self.player)
            # проверка gameover
            if self.player.health <= 0:
                self.player = Player("чувачок.png", 50, 500)
            # отрисовка фона
            self.current_location.draw(self.screen)
            # отрисовка персонажа
            self.player.draw(self.screen)
            # отрисовка сердечек
            for i in range(self.player.health):
                d = 10
                x = 20 + self.heart.get_width() * i + d * i
                y = 20
                self.screen.blit(self.heart, (x, y))
            pg.display.flip()

            # обработка событий
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    return
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        return
                    if event.key == pg.K_SPACE:
                        # активируем прыжок
                        self.player.start_jumping()
