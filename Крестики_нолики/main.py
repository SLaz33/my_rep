# Прописываем игровое поле в виде функции:
field = [[" "] * 3 for i in range(3)]
def demonstration():
    print()
    print(f"        0     1     2   ")
    print("     -------------------")
    print(f"0    |  {field[0][0]}  |  {field[0][1]}  |  {field[0][2]}  |")
    print("     -------------------")
    print(f"1    |  {field[1][0]}  |  {field[1][1]}  |  {field[1][2]}  |")
    print("     -------------------")
    print(f"2    |  {field[2][0]}  |  {field[2][1]}  |  {field[2][2]}  |")
    print("     -------------------")

#Прописываем функцию реализации хода игрока с проверкой ячеек

def move():
    while True:
        x, y = map(int,input("Введите координаты клетки через пробел:    ").split())
        if 0 <= x <= 2 and 0 <= y <= 2:
            if field[x][y] == ' ':
                return x, y
            else:
                print('Эта клетка уже занята, выберите свободную')
        else:
            print('Координаты вне диапазона, выберите координаты в пределах поля')

def check():
    win_comb = [
    ((0, 0), (0, 1), (0, 2)),
    ((1, 0), (1, 1), (1, 2)),
    ((2, 0), (2, 1), (2, 2)),
    ((0, 0), (1, 0), (2, 0)),
    ((0, 1), (1, 1), (2, 1)),
    ((0, 2), (1, 2), (2, 2)),
    ((0, 0), (1, 1), (2, 2)),
    ((0, 2), (1, 1), (2, 0))
    ]
    for comb in win_comb:
        comb_symbols = []
        for x in comb:
            comb_symbols.append(field[x[0]][x[1]])
        if comb_symbols == ['x', 'x', 'x']:
            demonstration()
            print('Выиграл Х, поздравляем!')
            return True
            break
        if comb_symbols == ['0', '0', '0']:
            demonstration()
            print('Выиграл 0, поздравляем!')
            return True
    return False

# Реализуем процесс игры с использованием двух описанных выше функций

print('Добро пожаловать в игру Крестики-нолики!')
print('Для совершения хода вводите координаты клетки игрового поля')
print('Первое число - номер строки, второе число - номер столбца')
move_num = 0
while True:
    move_num += 1
    demonstration()
    if move_num % 2 == 1:           # Здесь реализуем указание очередности хода
        print('Сейчас ходит Х')
    else:
        print('Сейчас ходит 0')
    x, y = move()

    if move_num % 2 == 1:           # Здесь реализуем запись нужного символа в ячейку
        field[x][y] = 'x'
    else:
        field[x][y] = '0'
    if check():             # Организуем проверку победы и остановку игры в случае ее наличия
        break

    if move_num == 9:
        print('Ничья')
        break
# вношу изменения
