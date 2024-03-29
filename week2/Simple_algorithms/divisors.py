"""Задача 1 - Списък от всички делители на едно число.
Ако имаме едно цяло число n, то всички делети на това число са тези числа между 1 и n - 1, които се делят на n без остатък.

Например, ако n = 6, то всички делители са:

1, защото 6 % 1 == 0
2, защото 6 % 2 == 0
3, защото 6 % 3 == 0
Във файл divisors.py, напишете програма, която:

Чете едно цяло число n
Изкарва списък от всички делители на n, без самото n.

"""

n = int(input('Enter number: '))

start, small_n, divisors = 1, n - 1, []

while start <= small_n:
    if n % start == 0:
        divisors += [start]

    start += 1

print('Divisors: ' + str(divisors))
