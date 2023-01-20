"""Задача 13 - Факториел
Във файл factorial.py, напишете програма, която:

Чете едно число n от клавиатурата.
Изкарва резултатът от n!, което се чете като "n факториел"
n! предсталява произведението на всички числа между 1 и n включително.

Например:

5! = 1 * 2 * 3 * 4 * 5 = 120
1! = 1
0! = 1 - това е специален случай.
20! = 2 342 902 008 176 640 000

"""

number = int(input('Enter number: '))

start = 1

total_num = 1

while start <= number:

    total_num *= start

    start += 1

    print(start)

    print('The product of the numbers in interval of 1 to ' + str(number) + ' is ' + str(total_num))
