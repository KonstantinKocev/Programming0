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

strings = ["python",
           "gogo",
           "perl",
           "java",
           "haskell",
           "ruby0nRails"]


def string_matrix(lenght_limit, string):
    the_matrix = []
    new_string = ""
    delimiter = " | "
    letter_string = ""

    for letter in range(len(string)):
        the_matrix += [string[letter]]

    current_word = ""
    result_words = []
    for word in the_matrix:
        if len(word) >= lenght_limit:
            current_word = word[:lenght_limit]
        else:
            current_word = word + (lenght_limit - len(word)) * "X"
        result_words += [current_word]

    new_new_string = ""

    for word in result_words:
        word += "\n"
        for letter in word:
            new_string += letter + delimiter

        for index in new_string:
            if index == "\n":
                new_new_string = new_new_string[:-1]

    for i in new_string[::-1]:
        if i == "\n":
            new_new_string = new_new_string[:-1]
        new_new_string += i

    return "| " + new_new_string[::-1][:-2]


print(string_matrix(6, strings))
