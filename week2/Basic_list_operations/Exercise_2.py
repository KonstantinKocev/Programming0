"""Задача 2 - Добавяне на елементи към списък
Нека да имаме следния списък:

languages = ["Python", "Ruby"]
Напишете изрази или statements в Python REPL, които:

Добавят към списъка languages, след "Ruby", езиците C++, Java и C#.
Добавят като първи елемент в списъка languages, езикът Haskell
Добавят като последен елемент във вече променения списък с нещата отгоре, езикът Go.
След като сте променили списъкът languages с нещата от по-горе, напишете изрази, които:

Връщат първия елемент на списъка
Връщат втория елемент на списъка
Връщат петия елемент на списъка
Променят елемента със стойност "C#" с нова стойност - F#
Връщат последния елемент на списъка. Може ли да решите това чрез функцията len ?
След като сте готови и с тази задача, напишете израз, които проверяват дали:

Езикът Haskell се намира в списъка languages
Езикът Ruby се намира в списъка languages
Езикът Go се намира в списъка languages
Езикът Rust се намира в списъка languages

"""

# 1. Добавяме след "Ruby", езиците C++, Java и C#.

languages = ["Python", "Ruby", ]
languages = languages + ["C++", "Java", "C#"]
print(languages)


# 2. Добавяме като първи елемент в списъка languages, езикът Haskell.

languages[0] = "Haskell"
print(languages)


# 3. Добавяме като последен елемент във вече променения списък с нещата отгоре, езикът Go.

languages[4] = "Go"
print(languages)


# 4. Връшаме първия, втория и петия елемент на списъка.

languages[0] = "Python"
languages[1] = "Ruby"
languages[4] = "C#"
print(languages)

#or

print(languages[0])
print(languages[1])
print(languages[4])


# 5. Променяме елемента със стойност "C#" с нова стойност - F#

languages[4] = "F#"
print(languages)

# 6. Проверяваме дали:

    #Езикът Haskell се намира в списъка languages
    #Езикът Ruby се намира в списъка languages
    #Езикът Go се намира в списъка languages
    #Езикът Rust се намира в списъка languages

if "Haskell" in languages:
    print(languages)
if "Ruby" in languages:
    print(languages)
if "Go" in languages:
    print(languages)
if "Rust" in languages:
    print(languages)