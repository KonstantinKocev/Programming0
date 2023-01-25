"""Броене на думи
Във файл count_words.py, напишете функция count_words(words), която:

Взима списък от низове words
Връща речник, който има следния вид:
{
  "word": count_of_that_word
}
За всеки елемент от списъка, се пази броят на неговите срещания в words.

Например: списъкът ["words", "are", "meaningful", "words", "words", "are"] ще създаде следния речник:

{
  "words": 3,
  "are": 2
  "meaningful": 1
}
Правете разлика между думи с главна и с малка буква.

"""

words = ["words", "are", "meaningful", "words", "words", "are"]


def counts_words(n):
    words_counter = 0
    are_counter = 0
    meaningful_counter = 0

    for i in words:
        if i == 'words':
            words_counter += 1
        elif i == 'are':
            are_counter += 1
        else:
            meaningful_counter += 1
    return {'words': words_counter,
            'are': are_counter,
            'meaningful': meaningful_counter}


print(counts_words(words))
