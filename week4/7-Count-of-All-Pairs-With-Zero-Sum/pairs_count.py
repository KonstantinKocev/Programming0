"""Броят на всички двойки в списък, чиято сума е 0
Във файл pairs.py, напишете функция count_zero_pairs(numbers), която:

Взима списък от цели числа items
Връща броя на всички двойки числа в items, чиято сума е равна на 0.
Ако имаме двойка (a, b), чиято сума е равна на 0, то я пребройте само 1 път.
Вземете предвид и двойките, които се образуват от един и същи елемент в списъка, но ги преброете 1 път
Ако имаме numbers = [0, 2, -2, 5, 10], то двойките, чиято сума е равна на 0 са:

0, 0
2, -2
С обща бройка 2.

"""

numbers = [0, 2, -2, 5, 10]


def count_zero_pairs(n):
    result = []
    counter = 0
    for i in n:
        if i + numbers[counter + 1] == 0:
            result.append(i)
            result.append(numbers[counter])
        counter += 1
    return result


print(count_zero_pairs(numbers))