"""Задача 6 - Сумата на цифрите на 1 число
Във файл sum_digits.py, напишете програма, която

Чете от потребителя едно цяло число n
На екрана изкарва сумата на неговите цифри.
Например:

Ако n = 123 то сумата на цифрите му е 6
Ако n = 12321938218904893204892598342, то сумата е 129

"""

number = int(input('Enter number: '))

total_sum = 0

while number != 0:
    digit = number % 10

    total_sum = total_sum + digit
    print(total_sum)

    number = number // 10