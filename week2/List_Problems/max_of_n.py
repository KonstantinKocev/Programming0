"""Задача 5 - Максималното число, въведено от потребител.
Във файл max_of_n.py, напишете програма, която:

Чете едно число n от потребителя.
На следващите n реда, чете по едно число от потребителя.
Накрая изкарва максималното число от всички въведени.
Примери:

Enter n: 6
-10
20
-30
5
0
100
Max is: 100

"""

n = int(input('Enter count of numbers: '))

start = 1
numbers = []

while start <= n:
    number = int(input('Enter number: '))
    numbers += [number]

    start += 1

max_num = numbers[0]

for number in numbers:
    if number > max_num:
        max_num = number

print('The biggest number is: ' + str(max_num))
