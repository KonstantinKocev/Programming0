"""Задача 4 - По-голямата последна цифра.
Във файл, който се казва bigger_last_digit.py, напишете програма, която:

Чете две цели числа от потребителя - n и m
На екрана извежда числото, което има по-голяма последна цифра от двете.
Ако последните цифри за равни, на екрана се извежда по-голямото число.
Например:

Ако имаме n = 1000 и m = 9, то резултатът на програмата е m, тъй като последната цифра на n е 0, а на m е 9 и 9 > 0.
Aко имаме n = 199 и m = 99, то резултатът е 199 - по-голямото число.
Подсказка

Колко е остатъка при деление на едно цяло число с 10?

"""

number_n = float(input('Enter number n: '))
number_m = float(input('Enter number m: '))

#if n %10 > m:
 #   print(n)
#elif m %10 > n:
 #   print(m)


last_n = number_n % 10
last_m = number_m % 10

#В случай, че двете числа не завършват на една и съща цифра. >>>

if last_n > last_m:
    print('The bigger number is n' + '(' + str(last_n) + ')')
elif last_m > last_n:
    print('The bigger number is m' + '(' + str(last_m) + ')')

#В случай, че двете числа завършват на една и съща цифра,
# се гледа кое първоначално въведено число е по-голямо. >>>

else:
    if number_n > number_m:
        print(number_n)
    elif number_m > number_n:
        print(number_m)