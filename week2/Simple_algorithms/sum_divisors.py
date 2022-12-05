"""Задача 2 - Сумата на всички делитети на едно число
Във файл sum_divisors.py, напишете програма, която:

Чете едно число n
Изкарва сумата на всички негови делители, без n.
Например, ако n = 6, сумата на делитете е 1 + 2 + 3 = 6

"""

n = int(input('Enter number: '))

start  = 1
small_n = n - 1
divisors = []

while start <= small_n:
    if n % start == 0:
        divisors += [start]

    start += 1

print('Divisors: ' + str(divisors))

sum_divisors = 0

for numbers in divisors:
    sum_divisors += numbers

print('The sum of divisors: ' + str(sum_divisors))
