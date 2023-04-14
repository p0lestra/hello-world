def print_play_field(field):
    print('   0 1 2')
    for i in range(3):
        print(f'{i} ', *field[i])


def get_coordinates(field, element_is_cross):
    while True:
        coordinates = input(
            'Введите координаты по X и Y для хода ' + ('крестиком: ' if element_is_cross else 'ноликом: ')).split()
        if len(coordinates) != 2:  # Проверка ввода
            print('Нужно ввести два числа X и Y')
        elif field[int(coordinates[1])][int(coordinates[0])] != '-':  # Проверка на свободную ячейку
            print('Ячейка занята')
        elif not coordinates[0].isnumeric() and coordinates[1].isnumeric():  # Проверка на положительность
            print('Числа должны быть положительными')
        elif not coordinates[0] in range(3) and coordinates[1] in range(3):
            print('Числа должны быть в диапозоне от 0 до 2')
        else:
            return int(coordinates[1]), int(coordinates[0])


def win(field):
    for i in range(3):
        if field[i][i] != '-' and (
                field[0][i] == field[1][i] == field[2][i] or field[i][0] == field[i][1] == field[i][2]):
            return True
        if field[1][1] != '-' and (
                field[0][0] == field[1][1] == field[2][2] or field[0][2] == field[1][1] == field[2][0]):
            return True
    return False


play_field = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
isCross = True
moves_count = 0

while moves_count < 9:
    print_play_field(play_field)
    x, y = get_coordinates(play_field, isCross)
    play_field[x][y] = 'x' if isCross else 'o'
    if win(play_field):
        print_play_field(play_field)
        print('Выиграли крестики' if isCross else 'Выиграли нолики')
        break
    isCross = not isCross
    moves_count += 1

