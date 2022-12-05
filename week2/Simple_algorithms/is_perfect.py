"""Задача 3 - Дали едно число е перфектно
Едно цяло число, наричаме перфектно, ако сумата на неговите делители, без самото число, е равно на самото число.

Например, числото 6 е перфектно, защото сумата на неговите делители е 6.
Друго перфеткно число е 28, което има сума на делителите: 1 + 2 + 4 + 7 + 14 = 28
Следващото перфектно число е 496.
Във файл is_perfect.py, напишете програма, която:

Чете едно число n от клавиатурата
Казва дали това число е перфектно или не.

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


if sum_divisors == n:
    print('The number is perfect!')
else:
    print('The number is not perfect!')
