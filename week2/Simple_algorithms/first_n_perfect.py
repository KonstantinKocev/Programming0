"""Задача 4 - Първите n на брой перфектни числа.
Това е трудна задача!

Във файл first_n_perfect.py, напишете програма, която:

Чете едно цяло число n
На екрана изкарва първите n на брой перфектни числа.
Например, ако n = 3, то първите 3 перфектни числа са:

6
28
496
Ако n = 6, това са:

6
28
496
8128
33550336
8589869056

"""

n = int(input('Enter number: '))

start = 6
count = 1
small_n = n - 1

while True:

    divisors = []

    while count <= small_n:
        if n % count == 0:
            divisors += [start]

        count += 1

    print(divisors)


    while n > 0:
        if start == sum(divisors):
            print(start)
            n -= 1
            start += 1

        start += 1

    if n == 0:
        break

    print(start)

