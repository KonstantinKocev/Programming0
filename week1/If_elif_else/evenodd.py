"""Задача 5 - Четно или нечетно?
Във файла evenodd.py, напишете програма, която:

Чете от потребителя дадено число
Отпечатва на екрана дали това число е четнои ли нечетно.
Едно число е четно (even), ако се дели на 2 без остатък. Иначе е нечетно (odd).

Примерно използване:

Enter number: 5
5 is odd.
Enter number: 4
4 is even.

"""


number = input('Enter number: ')
number = int(number)

if number % 2 == 0:
    print(str(number) + ' is even')
else:
    print(str(number) + ' is odd')