"""Магически квадрат
Казваме, че един квадрат е магически, ако е равна сумата на всичките елементи в:

Всеки ред
Всяка колона
Главния диагонал
Вторичния диагонал
Например, следния квадрат е магически:

23, 28, 21
22, 24, 26
27, 20, 25
Един квадрат всъщност представлява структура, в която се различават редове и колони.

В горния пример имаме:

Първият ред е със сума на елементите 23 + 28 + 21 = 72
Вторият ред е със сума на елементите 22 + 24 + 26 = 72
Третия ред е със сума на елементите 27 + 20 + 25 = 72
Първата колона е със сума на елементите 23 + 22 + 27 = 72
Втората колона е със сума на елементите 28 + 24 + 20 = 72
Третата колона е със сума на елементите 21 + 26 + 25 = 72
Главния диагонал е със сума на елементите 23 + 24 + 26 = 72
Вторичния диагонал е със сума на елементите 21  + 24 + 27 = 72
Следния квадрат не е магически:

1, 2, 3
4, 5, 6
7, 8, 9
В нашата програма, квадратът ще бъде представен като списък от списъци

Във файл magic.py, напишете функция magic_square(square), която взима един квадрат и връща True, ако той е магически. Иначe връща False.

Предните два примера могат да се изразят така:


square1 = [ [23, 28, 21],
            [22, 24, 26],
            [27, 20, 25] ]



square2 = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]

"""


def magic_square(square):
    value = sum(square[0])
    for row in square:
        current_value = sum(row)
        if current_value != value:
            return False

    for col_index in range(len(square)):
        current_value = iter_col(col_index, square)
        if current_value != value:
            return False

    current_value = diagonal_right_down(square)
    if current_value != value:
        return False

    current_value = diagonal_left_down(square)
    if current_value != value:
        return False

    return True


def iter_col(col_index, square):
    return sum([square[row][col_index] for row in range(len(square))])


def diagonal_right_down(square):
    return sum(square[index][index] for index in range(len(square)))


def diagonal_left_down(square):
    return sum([square[len(square) - 1 - index][index] for index in range(len(square))[::-1]])


good_example = [
    [23, 28, 21],
    [22, 24, 26],
    [27, 20, 25]
]

bad_example = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(magic_square(good_example))
print(magic_square(bad_example))
