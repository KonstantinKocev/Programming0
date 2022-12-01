"""Задача 7 - Сумата на цифрите на всички числа между N и M
Във файл sum_digits_interval.py, напишете програма, която:

Чете две цели числа N и M от потребителя.
Изкарва на екрана, за всяко число n между N и M включително, сумата на цифрите на n
Например:

Enter N: 1
Enter M: 15
Sum of digits of 1 = 1
Sum of digits of 2 = 2
Sum of digits of 3 = 3
Sum of digits of 4 = 4
Sum of digits of 5 = 5
Sum of digits of 6 = 6
Sum of digits of 7 = 7
Sum of digits of 8 = 8
Sum of digits of 9 = 9
Sum of digits of 10 = 1
Sum of digits of 11 = 2
Sum of digits of 12 = 3
Sum of digits of 13 = 4
Sum of digits of 14 = 5
Sum of digits of 15 = 6

"""

number1 = int(input('Enter number for n: '))
number2 = int(input('Enter number for m: '))

low_board = 0
up_board = 0

if number1 < number2:
    low_board = number1
    up_board = number2
else:
    low_board = number2
    up_board = number1

start = low_board

while start <= up_board:
    n = start
    total_sum = 0
    while n != 0:
        digit = n % 10
        total_sum = total_sum + digit
        n = n // 10

    print('Total sum of digits of ' + str(start) + ' = ' + str(total_sum))
    start = start + 1
