"""Задача 1 - Четно число, по-голямо от 20.
Във файла evenover20.py, напишете програма, която:

Чете едно число от потребителя.
Ако числото е четно и е по-голямо от 20, изпринтете "Yes it is!"
В противен случай, изпринтете "No it isn't"

"""

number = input('Enter number: ')
number = int(number)

if number %2 == 0 and number > 20:
    print('Yes, it is!')
else:
    print("No, it isn't.")