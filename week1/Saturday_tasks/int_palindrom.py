"""Задача 11 - Дали число е палиндром?
Във файл, int_palindrom.py, напишете програма, която:

Чете едно цяло число n от потребителя
Изкарва на екрана съобщение, ако числото е палиндром - The number is palindrom
В противен случай - The number is not palindrom
Едно число е палиндром, ако записано на обратно (започвайки в последната цифра), то числото е същото.

Например 121 и 1001 сa палиндроми.

"""

number = int(input('Enter number: '))

num1 = number % 10
number = number // 10

num2 = number % 10
number = number // 10

num3 = number % 10
number = number // 10

if num1 != num2 and num1 == num3:
    print('The number ' + str(num1) + str(num2) + str(num3) + ' is palindrom.')
else:
    print('The number in not palindrom.')
