"""Задача 2 - Игра на Зарове.
Във файл, който се казва dice_game.py, напишете програма, която прави следното:

Чете от потребител едно число N, което ще е броят на страните на зара
Чете името на първия играч.
Чете името на втория играч.
Хвърля зарове за първия и втория играч.
Имаме следните условия:

Играчът с по-голямо число, побежадава в играта. Програмата трябва да отпечата името на победителя"
Ако хвърлят едно и също число, програмата казва, че има равенство.
Примерно използване:

Enter dice side: 10
Enter player1 name: Rado
Enter player2 name: Ivo
Rado rolls 10
Ivo rolls 1
Rado wins!

"""
from random import randint

dice_sides = input('Enter dice sides: ')
dice_sides = int(dice_sides)

player1_name = input('Player 1 name: ')
player2_name = input('Player 2 name: ')

player1_dice = randint(1, dice_sides)
player2_dice = randint(1, dice_sides)

print(player1_name + ' rolls ' + str(player1_dice))
print(player2_name + ' rolls ' + str(player2_dice))

if player1_dice > player2_dice:
    print(player1_name + ' wins!')
elif player2_dice > player1_dice:
    print(player2_name + ' wins!')
elif player2_dice == player1_dice:
    print('Tie!')
