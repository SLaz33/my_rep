from random import randint
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
    def dots(self):
        ship_dots = []                              # здесь будем хранить списко точек корабля
        for i in range(self.l):           # в цикле делаем число шагов, равное длине корабля,
            cur_x = self.begin.x          # из точки-начала; все полученные точки
            cur_y = self.begin.y          # заносим в список - получаем "тело" корабля

            if self.n == 0:
                cur_x += i

            elif self.n == 1:
                cur_y += i

            ship_dots.append(Dot(cur_x, cur_y))

        return ship_dots                # возвращаем "тело" - список точек, где "стоит" корабль

    def is_hit(self, shot):         # проверяем, есть ли попадание
        return shot in self.dots

class Board:
    def __init__(self, hid=False, size = 6):           #задаём класс игрового поля
        self.size = size
        self.hid = hid
        self.ships_hitten = 0
        self.field = [[" "] * size for _ in range(size)]
        self.dots_busy = []
        self.ships = []

    def __str__(self):                                        #метод вывода поля на печать
        res = ""
        res += "  | 1 | 2 | 3 | 4 | 5 | 6 |"
        for i, row in enumerate(self.field):
            res += f"\n{i + 1} | " + " | ".join(row) + " |"

        if self.hid:
            res = res.replace("■", " ")
        return res

    def out(self, d):                                    #метод проверки нахождения точки в поле
        return not ((0 <= d.x < self.size) and (0 <= d.y < self.size))

    def contour(self, ship, verb = False):          #метод раасставления занятых точек
        border = [                                #вокруг корабля
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for d in ship.dots:
            for dx, dy in border:
                cur = Dot(d.x + dx, d.y + dy)
                if not (self.out(cur)) and cur not in self.dots_busy:
                    if verb:
                        self.field[cur.x][cur.y] = "."
                    self.dots_busy.append(cur)

    def ship_add(self, ship):                         #метод добавления кораблей на поле
        for d in ship.dots:
            if self.out(d) or d in self.dots_busy:
                raise WrongShipEx()
        for d in ship.dots:
            self.field[d.x][d.y] = "■"
            self.dots_busy.append(d)

        self.ships.append(ship)
        self.contour(ship)

    def shot(self, d):                          #метод выстрела по полю
        if self.out(d):                         #проверка попадания в поле
            raise OutBoardEx()

        if d in self.dots_busy:                 #проверка того, свободна ли точка
            raise DotRepeatEx()

        self.dots_busy.append(d)

        for ship in self.ships:
            if ship.is_hit(d):                        #если есть попадание
                ship.lives -= 1                       #уменьшаем количество жизней
                self.field[d.x][d.y] = "x"            # помечаем "х" клетку
                if ship.lives == 0:                   #если жизни кончились
                    self.ships_hitten += 1            #счетчик убитых кораблей +1
                    self.contour(ship, verb = True)
                    print("Убит!")                    #выводим сообщение
                    return False
                else:
                    print("Ранен!")
                    return True

        self.field[d.x][d.y] = "."          #помечаем точку, что туда уже был выстрел
        print("Мимо!")
        return False

    def begin(self):                # начале игры очищаем список занятых точек
        self.dots_busy = []

class Player:                                     #задаем родительский класс игрока
    def __init__(self, board, enemy_board):
        self.board = board
        self.enemy_board = enemy_board

    def ask(self):
        raise NotImplementedError()

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy_board.shot(target)
                return repeat
            except BoardEx as e:
                print(e)


class AI(Player):                                      #задаем производный класс игрока-AI
    def ask(self):
        d = Dot(randint(0, 5), randint(0, 5))
        print(f"Ход компьютера: {d.x + 1} {d.y + 1}")
        return d


class User(Player):                           #задаем производный класс игрока-человека
    def ask(self):
        while True:                #запрашиваем ввод координат
            cords = input("Введите координаты через пробел: ").split()

            if len(cords) != 2:  #проверяем наличие обеих координат
                print("Введите обе координаты!")
                continue

            x, y = cords

            if not (x.isdigit()) or not (y.isdigit()): #проверяем корректность
                print("Введите целые числа!")          #введенных координат
                continue

            x, y = int(x), int(y)

            return Dot(x - 1, y - 1)


class Game:                             #задаем класс игры
    def __init__(self):
        yb = self.random_board()      #создаем две доски
        eb = self.random_board()
        eb.hid = True

        self.ai = AI(eb, yb)         #создаем двух игроков
        self.pl = User(yb, eb)

    def get_board(self):                #попытка создать случайную доску
        ship_lens = [3, 2, 2, 1, 1, 1, 1]
        board = Board()
        attempt = 0
        for l in ship_lens:
            while True:
                attempt += 1
                if attempt > 2000:
                    return None
                ship = Ship(Dot(randint(0, 5), randint(0, 5)), l, randint(0, 1))
                try:
                    board.ship_add(ship)
                    break
                except WrongShipEx:
                    pass
        board.begin()
        return board

    def random_board(self):               #Повторяем попытки создать случайную доску,
        board = None                      #пока доска не будет создана
        while board is None:
            board = self.get_board()
        return board

    def greet(self):                    #метод-приветствие
        print("                   ")
        print("  Приветсвуем вас  ")
        print(" в игре морской бой")
        print("                   ")
        print(" Вводите координаты")
        print(" через пробел: x y ")
        print(" x - номер строки  ")
        print(" y - номер столбца ")

    def loop(self):                       #создаем метод игрового цикла
        turn = 0
        while True:
            print(" " * 20)
            print("Доска пользователя:")
            print(self.pl.board)
            print(" " * 20)
            print("Доска компьютера:")
            print(self.ai.board)
            print("-" * 20)
            if turn % 2 == 0:
                print("Ходит игрок")
                repeat = self.pl.move()
            else:
                print("Ходит компьютер")
                repeat = self.ai.move()
            if repeat:
                turn -= 1

            if self.ai.board.ships_hitten == 7:
                print(" " * 20)
                print("Вы порвали железяку, так держать!")
                break

            if self.pl.board.ships_hitten == 7:
                print(" " * 20)
                print("Машина оказалась сильнее!")
                break
            turn += 1

    def start(self):                      #задаем метод, который запускает
        self.greet()                      #приветствие и игровой цикл
        self.loop()

g = Game()
g.start()
