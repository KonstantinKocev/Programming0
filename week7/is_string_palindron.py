"""Най-якият палиндром!
Във файл is_string_palindrom.py напишете функция is_string_palindrom(string) , която приема стринг като аргумент и проверява дали той е палиндром, връщайки True или False.

Нещо е палиндром ако прочетено от ляво на дясно и прочетено от дясно на ляво е едно и също.

Пример: "капак" от ляво на дясно е "капак", а от дясно на ляво... отново е "капак" :)
Стрингът може дори да е цяло изречение с празни разстояния между думите или стринг със шпации в него. Празните разстояния не пречат на палиндромността му
В низа може да има и следните препинателни знаци: ",", ".", "!" и "?". Те не пречат на палиндромността на низа!
Не се интересуваме дали буквите са главни или малки. Програмата ни трябва да ги уеднакви.
Примери:

is_string_palindrom("Az obi4am ma4 i boza") --> трябва да върне True
is_string_palindrom("A Toyota!") --> трябва да върне True
is_string_palindrom("bozaaa") --> трябва да върне False
is_string_palindrom("    kapak!   ") --> трябва да върне True
Подсказки
За да превърнете един низ в низ само с малки букви, може да използвате следното нещо:

a = "A TOYOTA!"
a = a.lower()

print(a)
# "a toyota!"
Като алгоритъм може да подходите така:

Махнете всички празни разстояния
Махнете всички препиналтени знаци
Направете всички букви в стринга малки.
Ако обърнат е същия, значи е палиндром

"""

a = "Az obi4am ma4 i boza"
a = a.lower()


def is_string_palindrom(string):
    new_string = ""
    all_letters = "abcdefghijklmnopqrstuvwxyz1234567890,.!?"
    for letter in string:
        if letter in all_letters:
            new_string += letter
    rev_string = new_string[::-1]
    print(new_string, "|", rev_string)
    if rev_string == new_string:
        return True
    return False


print(is_string_palindrom(a))
