"""Задача 4 - Какви са числата в даден интервал. Четни или нечетни?
Във файл, който се казва even_odd_interval.py, напишете програма, която:

Чете две числа от потребителя, които представляват интервал от цели числа.
За всяко число от интервала, изкарва на екрана самото число и съответно текст дали е четно или не.
Например:

Enter a: 1
Enter b: 5
1 - odd
2 - even
3 - odd
4 - even
5 - odd

"""

a = int(input('Enter a: '))
b = int(input('Enter b: '))

while a <= b:
    if a %2 == 1:
        print(str(a) + ' odd')
    elif a %2 == 0:
        print(str(a) + ' even')

    a += 1