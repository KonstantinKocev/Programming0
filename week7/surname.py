"""Във файл surname.py напишете функция taken_name(surname_husband, surname_wife), която:
приема два аргумента - фамилията на мъжа и фамилията на жената.
функцията връща True, ако жената е взела фамилията на мъжа и False, ако не е.
Примери:

"""


def taken_name(surname_husband, surname_wife):
    if surname_husband in surname_wife:
        return True
    return False


print(taken_name("Petrov", "Ivanova-Petrova"))
