"""Задача 2 - Четене на променлив брой вход от потребителя.
Във файл read_n_numbers.py имаме следната програма:

n = input("Enter count of numbers: ")
n = int(n)

count = 1
numbers = []

while count <= n:
    number = input("Enter number: ")
    number = int(number)

    numbers = numbers + [number]

    count += 1

print(numbers)
По този начин може да прочетем променлив брой вход от потребителя.

Въведи числото n и на следващите n реда ще има по 1 число

Пуснете програмата и я разучете!

"""

n = int(input("Enter count of numbers: "))

count = 1
numbers = []

while count <= n:
    number = int(input("Enter number: "))

    numbers += [number]

    count += 1

print(numbers)

# С всяко обхождане с while пишем ново число, което бива вкарано в списък.