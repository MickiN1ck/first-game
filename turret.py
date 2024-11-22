import pygame as pg
from shot import Shot
from player import Player


class Turret:
    def __init__(self, image: str, x: int, y: int, shot: str, sound: pg.mixer.Sound):
        self.sound = sound
        self.sound.set_volume(0.4)
        self.picture = pg.image.load(f"картинки/{image}")
        self.body_rect = pg.rect.Rect(x, y,
                                      self.picture.get_width(), self.picture.get_height())
        self.shots = []
        self.shot_pic = pg.image.load(f"картинки/{shot}")
        self.fire_time = 120
        self.fps_counter = 0

    def draw(self, screen: pg.Surface):
        screen.blit(self.picture, (self.body_rect.x, self.body_rect.y))
        for shot in self.shots:
            shot.draw(screen)

    def fire(self):
        self.shots.append(Shot(self.shot_pic, self.body_rect.x, self.body_rect.y + 27))
        self.sound.play()

    def update(self, player: Player):
        # добавить пули
        self.fps_counter += 1
        if self.fps_counter == self.fire_time:
            self.fire()
            self.fps_counter = 0
        for shot in self.shots:
            # is_hit попала или нет пуля в персонажа
            if shot.is_hit(player):
                # здоровье отнимается

                self.shots.remove(shot)
                continue
            shot.move()
            # удалять пулю когда ее правая сторона заходит за левую границу экрана
            if shot.body_rect.right <= 0:
                self.shots.remove(shot)
