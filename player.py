import pygame as pg


class Player:
    def __init__(self, image: str, x: int, y: int):
        self.health = 5  # здоровье
        self.skin = pg.image.load(f"картинки/{image}")  # картинка персонажа
        self.speed = 5  # скорость вправо/влево
        self.high_speed = 5
        self.body_rect = pg.rect.Rect(x, y,
                                      self.skin.get_width(), self.skin.get_height())  # граница персонажа
        self.is_jumping = False  # прыгает ли сейчас персонаж?
        self.max_jump_speed = 23  # максимальная скорость прыжка
        self.jump_speed = self.max_jump_speed  # текущая скорость прыжка
        self.gravity_speed = 0  # текущая скорость гравитации
        self.grounded = False  # стоит на земле

    def draw(self, screen: pg.Surface):
        """
        функция отрисовывает персонажа и его обводку
        :param screen:
        :return:
        """
        screen.blit(self.skin, (self.body_rect.x, self.body_rect.y))
        # pg.draw.rect(screen, "red", self.body_rect, 2)

    def control(self):
        """
        функция для управления персонажем (право-лево)
        :return:
        """
        pressed = pg.key.get_pressed()
        if pressed[pg.K_a]:
            self.body_rect.x -= self.speed
        if pressed[pg.K_d]:
            self.body_rect.x += self.speed
        if pressed[pg.K_LSHIFT] and pressed[pg.K_d]:
            self.body_rect.x += self.high_speed
        if pressed[pg.K_LSHIFT] and pressed[pg.K_a]:
            self.body_rect.x -= self.high_speed

    def gravity(self):
        """
        функция для создания гравитации (толкает персонажа вниз)
        :return:
        """
        if not self.grounded:
            self.gravity_speed += 1
            self.body_rect.y += self.gravity_speed
            if self.body_rect.bottom > 750:
                self.body_rect.y = 750 - self.skin.get_height()
                self.gravity_speed = 0
                self.grounded = True
            elif self.body_rect.bottom == 750:
                self.gravity_speed = 0
                self.grounded = True

    # апдейт вызывается каждый кадр
    def update(self):
        """
        обновляет состояние персонажа каждый кадр
        :return:
        """
        # управление персонажем в стороны
        self.control()
        # движение персонажа по вертикали
        self.vert_move()

    def start_jumping(self):
        """
        начало прыжка
        :return:
        """
        if not self.is_jumping and self.grounded:
            self.is_jumping = True

    def get_damage(self, damage: int):
        self.health -= damage

    def vert_move(self):
        """
        движение персонажа по вертикали
        :return:
        """
        # если персонаж прыгает
        if self.is_jumping:
            self.grounded = False
            # перемещение вверх
            self.body_rect.y -= self.jump_speed
            # уменьшаем скорость
            self.jump_speed -= 1
            # если скорость равна нулю
            if self.jump_speed == 0:
                # выставляем скорость на первоначальное значение
                self.jump_speed = self.max_jump_speed
                # прекращаем прыжок
                self.is_jumping = False

        else:
            self.gravity()
