"""Задача 1 - Легални по американски.
Във файл, който се казва legal.py, напишете програма, която прави следното:

Чете от потребителя число, което отговаря на годините му.
Ако годините са >= 21, му казва, че е легален.
Иначе му казва, че е нелегален!
Примерно използване:

You age? 18
Your are illegal here.
Your age? 21
You are legal here.

"""

age  = input('Your age: ')
age = int(age)

if age < 21:
    print('You are illegal here.')
else:
    print('You are legal here.')
