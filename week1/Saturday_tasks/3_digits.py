"""Задача 8 - Число от 3 цифри
Във файл 3_digits.py, напишете програма, която:

Чете 3 цифри (цели числа с 1 цифра) от потребителя.
Изкарва на екрана цялото число, което е съставено от тези цифри, започващо с първата въведена.
Например:

Enter a: 5
Enter b: 0
Enter c: 1
501

"""

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

number = num1 * 100 + num2 * 10 + num3

print(number)