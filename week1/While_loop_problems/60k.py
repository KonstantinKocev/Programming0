"""Задача 5 - 60 000 завъртания.
Във файл с име 60k.py, напишете програма, която:

Пуска безкраен цикъл, който увеличава даден брояч, започващ от 1.
Когато броячът стигне 60 000, цикълът се прекъсва чрез break
Изпринтва се на екрана фактът, че програмата е завършила.

"""

number = 1
number = int(number)

while number <= 60000:
    print(number)

    number = number + 1

    if number == 60000:
        print('Program end.')
