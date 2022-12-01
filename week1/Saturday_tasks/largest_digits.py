"""Задача 9 - Най-голямото и най-малкото число, съставено от 3 цифри.
Във файл largest_3_digits.py, напишете програма, която:

Чете едно цяло трицифрено число n от потребителя
На екрана изкарва най-голямото число, което може да се получи със същите 3 цифри на n
На екрана изкарва най-малкото число, което може да се получи със същите 3 цифри на n
Например, ако n = 153, най-голямото число със същите цифри е 531, а най-малкото: 135.

"""

n = int(input('Enter number:'))

a = n % 10
n = n // 10

b = n % 10
n = n // 10

c = n % 10
n = n // 10


largest = a

if b >= a and b >= c:
    largest = b
if c >= a and c >= b:
    largest = c


smallest = a

if b <= a and b <= c:
    smallest = b
if c <= a and c <= b:
    smallest = c


middle = c

if (largest == c and smallest == b) or (largest == b and smallest == c):
    middle = a
elif (largest == a and smallest == c) or (largest == c and smallest == a):
    middle = b


smallest_num = smallest * 100 + middle * 10 + largest
max_num = largest * 100 + middle * 10 + smallest

print('The largest number with these digits is: ' + str(max_num))
print('The smallest number with these digits is: ' + str(smallest_num))
