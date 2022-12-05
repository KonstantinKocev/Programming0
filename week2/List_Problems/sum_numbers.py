"""Задача 4 - Сумата на всички числа, въведени от потребителя
Във файл sum_numbers.py, напишете програма, която:

Чете едно число n от потребителя
На следващите n редам чете по едно число от потребителя
Накрая изкарва сумата на всички числа, които потребителят е въвел.
Пример

Enter n: 5
1
5
-10
20
0
The sum is: 16

"""

number = int(input('Enter count of number: '))

start = 1

total_num = []

# Вкарваме n числа от потребителя и ги поставяме в списък [num].

while start <= number:
    num = int(input())
    total_num += [num]

    start += 1

# Обхождаме списъка [num] с цикъл for и изкарваме сумата на числата.

total_sum = 0

for num in total_num:
    total_sum += num

print('The sum is: ' + str(total_sum))
