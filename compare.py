"""Задача 4 - Сравнение на числа
Във файл, който се казва compare.py, напишете следната програма:

Чете две числа от потребителя.
И спрямо следните условия, казва:

Кое от двете числа е по-голямо?
Ако са равни, казва, че числата са равни.
Примерно използване:

Enter a: 5
Enter b: 6
b(6) is bigger than a(5)!
или:

Enter a: 5
Enter b: 5
a(5) is equal to b(5)

"""

a = input('Enter a: ')
a = int(a)
b = input('Enter b: ')
b = int(b)

if a > b:
    print('a' + '(' + str(a) + ')' +' is bigger than b' + '(' + str(b) + ')')
elif b > a:
    print('b' + '(' + str(b) + ')' + ' is bigger than a' + '(' + str(a) + ')')
elif a == b:
    print('a' + '(' + str(a) + ')' +' is equal to b' + '(' + str(b) + ')')

