"""Задача 2 - Сумата на всички четни числа между 1 и N.
Във файла sum_of_evens.py напишете програма, която:

Чете едно число n от потребителя.
На екрана изкарва сумата на всички четни числа между 1 и n включително.
Едно число е четно, ако се дели на 2 без остатък:

if n % 2 == 0:
    print("n is even")

"""

n = int(input('Enter number n: '))

start = 1

total = 0

while start <= n:
    if start %2 == 0:
        total = total + start
        print(total)

    start = start + 1
