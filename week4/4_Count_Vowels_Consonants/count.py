"""рой на гласни и съгласни
Във файл count.py напишете функция count_vowels_consonants(word), която:

Взима един низ word
Връща речник, в който има два ключа - "vowels" и "consonants"
Срещу всеки ключ, трябва да стои съответния брой на гласни и съгласни букви в думата.
Бройте както главните, така и малките гласни и съгласни букви:

Гласните са "aeiouyAEIOUY"
Съгласните са "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
Например:

'>>> count_vowels_consonants("aaaAcccD")'
{
  "vowels": 4,
  "consonants": 4
}

"""

vowels = "aeiouyAEIOUY"
consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"

n = input('Enter your word: ')


def count_vowels_consonants(word):
    vowels_counter = 0
    consonants_counter = 0
    for i in word:
        if i in vowels:
            vowels_counter += 1
        elif i in consonants:
            consonants_counter += 1

    return {'vowels': vowels_counter, 'consonants': consonants_counter}


print(count_vowels_consonants(n))