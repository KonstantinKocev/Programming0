"""Задача 3 - От потребителя до потребителя.
Във файл, който се казва user_to_user.py, напишете програма, която:

Чете едно число от потребителя - a
Чете второ число от потребителя - b
Принти на екрана всички цели числя в интервала [a, b]
Програмата съобразява кое от двете числа е по-малко. При вход a = 10, b = 5, трябва да се изпринтят всички числа от [5, 10]
Примери:

Enter a: 5
Enter b: 15
5
6
7
8
9
10
11
12
13
14
15
Или:

Enter a: 10
Enter b: 7
7
8
9
10

"""

start = int(input('Enter start number: '))
end = int(input('Enter end number: '))

variable = start

while variable <= end:
    print(variable)

    variable += 1

while end >= start:
    print(end)

    end -= 1