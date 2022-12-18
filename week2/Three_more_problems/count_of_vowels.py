"""Задача 3 - Брой на срещанията на гласните букви в низ.
Имаме следната задача:

Дават ни някакъв низ (string) на английски език от входа
Трябва да кажем броят на гласните букви в низа, като броим и главни и малки букви.
Наприме в низа "I am a very very man" имаме 8 гласни - I, a, a, e, y, e, y, a.

Всички гласни букви, големи и малки, в английската азбука са: "aeiouyAEIOUY"

Във файл count_vowels.py, напишете програма, която:

Чете един низ от потребителския вход
Изкарва на екрана броят на големите и малките гласни в низа.
Ето няколко примера:

"There is a very long line of people behind that building" - 19
"Aaarrhghh!" - 3
"sssssssssSSssS!" - 0
Важни неща, които трябва да знаете, за да решите задачата
Низовете в Python представляват списък от символи (characters).

Това означава, че може да обходите един низ символ по символ чрез for:

string = "asl_pls"

# ch stands for character

for ch in string:
    print(ch)
Това ще изкара на екрана:

a
s
l
_
p
l
s
Което означава, че в ch се намира поредния символ на низа.

Алгоритъм за решаване на задачата
Ако искаш сам/а да се пробваш, не продължавай да четеш надолу!

Слагаме брояч на гласните counter = 0
Дефинираме си променлива, която е низ с всички гласни: vowels = "aeiouyAEIOUY"
Обхождаме въведения ни вход чрез for ch in string:
Ако ch in vowels е True - увеличаваме counter с 1
Накрая имаме резултатът в counter

"""

n = input("Enter some text: ")

vowels = list("aeiouyAEIOUY")
start = 1
list_letter = []

while start <= 1:
    list_letter += [n]

    start += 1

for i in list_letter:
    print(list(i))

counter = 1

for v in i:
    if v in vowels:
        counter += 1

print(v)
print(counter)