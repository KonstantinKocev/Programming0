"""Задача 2 - От 1 до потребителя
Във файл, който се казва count_to_user.py, напишете програма, която:

Чете от потребителя 1 число - n.
Принтира всички числя от 1 до n
След което принтира всички числа от n до 1
Всяко принтиране да е на нов ред.
Примери:

Enter number: 6
1
2
3
4
5
6

"""

n = input('Enetr number: ')
n = int(n)

first = 1

while first <= n:
    print(first)

    first += 1

n = input('Enter number: ')
n = int(n)

while first >= n:
    print(first)

    first -= 1