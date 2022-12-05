"""Задача 6 - Минималното число, въведено от потребител.
Във файл min_of_n.py, напишете програма, която:

Чете едно число n от потребителя.
На следващите n реда, чете по едно число от потребителя.
Накрая изкарва мининалното число от всички въведени.
Примери:

Enter n: 6
-10
20
-30
5
0
100
Min is: -30

"""

n = int(input('Enter count of numbers: '))

start = 1
numbers = []

while start <= n:
    number = int(input('Enter number: '))
    numbers += [number]

    start += 1

min_num = numbers[0]

for number in numbers:
    if number < min_num:
        min_num = number

print('The smallest number is: ' + str(min_num))
