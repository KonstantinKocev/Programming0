"""Задача 8 - Брой на срещания на дадена дума.
Във файл words_count.py, напишете програма, която:

Чете на един ред от потребителя, дадена дума (string) word
Чете на следващия ред от потребителя едно число n
На следващите n реда, чете по 1 дума на ред.
Накрая, програмата изкарва броя на срещанията на думата word в тези n думи въведени от потребителя.
Примери:

Enter word: python
Enter n: 5
haskell
ruby
python
python
Go

python is found 2 times.

"""

n_word = input('Enter word: ')
n = int(input('Enetr count of words: '))

n_count = 1
words = []

while n_count <= n:
    word = input('Enter word:')
    words = words + [word]
    n_count += 1

word_numbers = 0

for word in words:
    if n_word == word:
        word_numbers += 1

print(n_word + ' found: ' + str(word_numbers) + ' times in ' + str(words))
