"""Вътрешен trim
След като решихме проблема с премахване на празните пространства от началото и края на даден низ, сега трябва да решим друг проблем - разстоянието между отделните думи, ако то е по-голямо от 1 шпация.

Във файл inner_trim.py напишете функция inner_trim(string), която взима низ и прави 2 неща:

trim-ва всички whitespace-ове от началото и края (това сме го решавали!)
Нормализира всички разстояния вътре в string, до точно 1.
"""


def inner_trim(string):
    counter = 0
    result = ""
    for i in string:
        if i == " ":
            counter += 1
        else:
            break
    result = string[counter:]
    new_string = ""
    flag = False
    for i in result[::-1]:
        if i != " ":
            flag = True
            new_string += i
        else:
            if flag:
                new_string += i

    words = []
    current_word = ""
    for letter in new_string:
        if letter != " ":
            current_word += letter
        else:
            if current_word != "":
                words += [current_word]
                current_word = ""

    words += [current_word]

    result = ""
    for i in words:
        result += i + " "
    result = result[:-1]

    return result[::-1]


print(inner_trim("  Python     Django   "))
