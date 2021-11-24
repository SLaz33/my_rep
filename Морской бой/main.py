class BoardEx(Exception):                       #задаём классы исключений
    pass

class OutBoardEx(BoardEx):
    def __str__(self):
        return "Ваш выстрел мимо доски!"

class DotRepeatEx(BoardEx):
    def __str__(self):
        return "Вы уже стреляли сюда"

class WrongShipEx(BoardEx):
    pass

class Dot:                                          #определяем класс точки
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):                        #задаём процедуру сравнения точек
        return self.x == other.x and self.y == other.y

    def __repr__(self):                              #задаём формат вывода точки
        return f"Dot({self.x}, {self.y})"


class Ship:
    def __init__(self, begin, l, n):       # Параметры корабля: начало(нос),длина,
        self.begin = begin                 # ориентация (0 - гориз., 1 - верт.)
        self.l = l                         # и количество жизней (равно длине)
        self.n = n
        self.lives = l

    @property
    def ship_dots(self):
        dots = []                              # здесь будем хранить списко точек корабля
        for i in range(self.l):           # в цикле делаем число шагов, равное длине корабля,
            cur_x = self.begin.x          # из точки-начала; все полученные точки
            cur_y = self.begin.y          # заносим в список - получаем "тело" корабля

            if self.n == 0:
                cur_x += i

            elif self.n == 1:
                cur_y += i

            dots.append(Dot(cur_x, cur_y))

        return dots                # возвращаем "тело" - список точек, где "стоит" корабль

    def is_hit(self, shot):         # проверяем, есть ли попадание
        return shot in self.ship_dots

s = Ship(Dot(1, 2), 5, 0)
print(s.ship_dots)
print(s.is_hit(Dot(2, 3)))