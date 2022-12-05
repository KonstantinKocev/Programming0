"""Задача 7 - Средно-аритметично от всички въведени числа.
Във файл avg.py, напишете програма, която:

Чете едно число n от потребителя.
На следващите n реда чете по едно число от потребителя.
Накрая изкарва средното аритметично на всички въведени числа.
Средното аритметично се определя като разделим сумата на всички числа върху техния брой

Примери:

Enter n: 4
1
3
2
7
Avg is 3.25

"""

n = int(input('Enter count of numbers: '))

start = 1
numbers = []

while start <= n:
    number = int(input('Enter number: '))

    numbers += [number]

    start += 1

sum_index = 0
list_len = len(numbers)

for number in numbers:
    sum_index = sum_index + number

avg = sum_index / list_len

print('The average number is: ' + str(avg))
