"""Задача 3 - Калкулатор
Във файл, който се казва calculator.py, напишете следната програма:

Чете от потребител, първото число a
Чете от потребител, второто число b
Чете от потребител, операцията oper, която може да е или +, -, *, и /.
Програмата трябва да направи следното нещо:

Изкарва на екрана резултатът от получения израз: a oper b.
Ако получи неизвестна операция, да каже за това.
Примерно използване:

Enter a: 5
Enter b: 10
Enter operation: +
Result is:
15
или

Enter a: 5
Enter b: 10
Enter operation: ^^
We do not support that operation.

"""

a = input('Enter a: ')
a = int(a)
b = input('Enter b: ')
b = int(b)

oper = input('Enter oper: ')

result = False

if oper == '+':
    result = a + b
elif oper == '-':
    result == a - b
elif oper == '*':
    result = a * b
elif oper == '/':
    result = a / b

if result != False:
    print('Result is ' + str(result))
else:
    print('We do not supprt that operation!')