"""Задача 1 - От 1 до 10 и от 10 до 1
Във файл, който се казва count_to_ten.py, напишете програма, която:

Принтира на екрана числата от 1 до 10 в нарастващ ред.
След което принтира числата от 10 до 1 в намаляващ ред.
Всяко число трябва да е на нов ред (В отделен print)
Примери:

1
2
3
4
5
6
7
8
9
10

"""

print('Counting from 1 to 10:')

first = 1
last = 10

while first <= last:
    print(first)

    first += 1

print('\nCounting from 10 to 1:')

first = 10
last = 1

while first >= last:
    print(first)

    first -= 1