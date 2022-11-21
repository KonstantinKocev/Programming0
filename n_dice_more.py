"""В файл, който се казва n_dice_more.py, напишете програма, която:

Чете от потребител едно цяло число N
Хвърля зарче с N страни и получава число между 1 и N
Хвърля зарчето още 1 път.
Хвърля зарчето 3ти път.
Програмата трябва да:

Отпечатва всеки път на екрана, когато хвърли за число
Накрая, трябва да отпечата сумата на 3те числа, които е получила след хвърляне на зарче.
Примерно използване:

Enter sides: 20
First roll:
10
Second roll:
5
Sum is:
15
"""

from random import randint

n = input("Enter dice sides: ")
n = int(n)

rolling_dice1 = randint(1, n)
rolling_dice2 = randint(1, n)
rolling_dice3 = randint(1, n)

print(rolling_dice1)
print(rolling_dice2)
print(rolling_dice3)

print(rolling_dice1 + rolling_dice2 + rolling_dice3)

