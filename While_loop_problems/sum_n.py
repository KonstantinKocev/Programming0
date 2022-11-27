"""Задача 6 - Сумата на числата от 1 до N
Във файл, с име sum_n.py, напишете програма, която:

Чете едно цяло число N от потребителя.
Принтира на екрана сумата на всички цели числа между 1 и N
Примери:

Enter N: 10
55

"""

number = int(input("Enter number: "))

total_sum = 0

start = 1

while start <= number:
    total_sum = total_sum + start

    start = start + 1

print("The sum is: " + str(total_sum))
