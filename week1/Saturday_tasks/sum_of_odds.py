"""Задача 3 - Сумата на всички нечетни числа между 1 и N
Във файла sum_of_odds.py напишете програма, която:

Чете едно число n от потребителя.
На екрана изкарва сумата на всички нечетни числа между 1 и n включително.
Едно число е нечетно, ако се дели на 2 с остатък 1:

if n % 2 == 1:
    print("n is odd")

"""

n = int(input('Enter number n: '))

start = 1

total = 0

while start <= n:
    if start %2 == 1:
        total = total + start
        print(total)

    start = start + 1