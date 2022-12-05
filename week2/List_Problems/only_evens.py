"""Задача 3 - Броят на четните числа от всички въведени от потребителя.
Във файл only_evens.py, напишете програма, която:

Чете едно число n от потребителя
На следващите n реда чете по едно число
Първо, програмата изкарва на екрана броят на четните числа.
Накрая принтира на екрана само четните числа, от въведените от потребителя
Пример:

Enter n: 5
2
5
6
8
9
Count of evens: 3
Evens are:
2
6
8

"""

n = int(input('Enter count of number: '))

num = 1
even_num = []

while num <= n:
    number = int(input('Enter number: '))
    if number % 2 == 0:
        even_num += [number]

    num += 1

print('Count of evens: ' + str(len(even_num)))
print('Evens are: ')

for even in even_num:
    print(even)