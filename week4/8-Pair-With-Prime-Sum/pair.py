"""Двойка числа със сума, която е просто число
Във файла pair.py, напишете функция prime_pair(numbers), която:

Взима един списък от цели числа numbers.
Връща True, ако поне една произволна двойка числа от списъка, дава сума, която е просто число.
Вземете всички двойки предвид - дори и тези, които са съставени от 1 елемент, участващ 2 пъти в двойката.
Например: numbers = [1, 2, 3, 4, 5], имаме поне една двойка 1, 2, която дава сума 3, което е просто число

"""

from random import randint


def prime_pair(x):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    counter = 0
    while counter <= len(numbers):
        sum_nums += (numbers[randint(numbers[0], len(numbers) - 1)] + numbers[randint(numbers[0], len(numbers) - 1)])
        counter += 1
    if sum_nums
    return


print(prime_pair([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))