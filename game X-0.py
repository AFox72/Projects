def privet():
    print("Игра крестики-нолики")
    print("формат ввода: x y")
    print("x - номер строки")
    print("y - номер столбца")

def pole():
    print("  | 0 | 1 | 2 |")
    print("_______________")
    for i, stroka in enumerate(igpole):
        ns = f"{i} | {' | '.join(stroka)} | "
        print(ns)
        print("_______________")

def hod():
    while True:
        h = input("Ходите: ").split()

        if len(h) != 2:
            print("Неправильный формат ввода, введите 2 координаты")
            continue

        x, y = h

        if not (x.isdigit()) or not (y.isdigit()):
            print("Введите числа")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Введите координаты, в диапозоне игрового поля")
            continue

        if igpole[x][y] != " ":
            print("Клетка занята, выбирете другую")
            continue

        return x, y

def pobeda():
    pob = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
           ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
           ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for k in pob:
        s = []
        for c in k:
            s.append(igpole[c[0]][c[1]])
        if s == ["X", "X", "X"]:
            print("Победил X")
            return True
        if s == ["O", "O", "O"]:
            print("Победил O")
            return True
    return False

privet()
igpole = [[" "] * 3 for i in range(3) ]
hody = 0
while True:
    hody += 1
    pole()
    if hody % 2 == 1:
        print("Ход Х")
    else:
        print("Ход О")

    x, y = hod()

    if hody % 2 == 1:
        igpole[x][y] = "X"
    else:
        igpole[x][y] = "O"

    if pobeda():
        break

    if hody == 9:
        print("Ничья")
        break