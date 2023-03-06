"""Подсписък
Във файла sublist.py, напишете функцията sublist(list1, list2), която проверява дали list1 е подсписък на list2.

Казваме, че един списък е подсписък на друг, ако всички негови елементи ги има като последователност в другия списък.

Например списъкът [1, 2, 3] е подсписък на [0, 0, 1, 2, 3, 5, 6].
Празният списък - [] - е подсписък на на всеки други списък.
Функцията sublist трябва да върне True или False

Примерни данни
["Python"] е подсписък на ["Python", "Django"]
["Python", "Django"] не е подсписък на ["Django", "Python"]
[1,2] e подсписък на [1, 0, 1, 2, 2]

"""


def sublist(list1, list2):
    some_shit = []
    counter = 0

    while counter > len(list1):

        counter += 1

    if list1 == some_shit:
        return True
    else:
        return False


list1 = [1, 2, 3]
list2 = [0, 0, 1, 2, 3, 5, 6]

print(sublist(list1, list2))
