"""Низова матрица
Във файл с име string_matrix.py, напишете програма,в която има следната функция string_matrix(matrix_width, strings).

Функцията взима като аргументи число и списък от стирнгове, а връща :

матрица, с размери подадето число и с елементи - char-овете на подадените стрингове.
на всеки ред от матрицата трябва да се намира само по един стринг. Ако дължината му е по-голяма от големината на матрицата, го отрежете до подходяща.
Ако е с по-малка дължина - допълнете реда на матрицата с "X".
Пример:

| p | y | t | h | o | n |
| g | o | g | o | X | X |
| p | e | r | l | X | X |
| j | a | v | a | X | X |
| h | a | s | k | e | l |
| r | u | b | y | O | n |
Подсказка
Вижте решението на Tic Tac Toe задачата

"""


strings = ["python", "gogo", "perl", "java", "haskell", "ruby0nRails"]

def string_matrix(number, string):
    the_matrix = []
    for i in string:
        row = join(" | ", i)
        row = "| " + row
        the_matrix +=[row]
    letter_counter = 0
    for letter in the_matrix:
        if letter in "abcdefghijklmnopqrstuvwxyz":
            letter_counter += 1
    if letter_counter < number:


def join(delimiter, items):
    new_string = ""
    for i in items:
        new_string += i + delimiter
    return new_string
