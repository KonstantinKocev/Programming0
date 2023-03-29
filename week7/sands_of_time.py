"""Пясъчен часовник
Лесно и просто, трябва да потребителя да каже едно число и програмата да му принтира пясъчен засовник с

Напитете програмата sands_of_time.py, която:

потребителя въвежда едно нечетно число N, което представлява широчината на пясъчния часовник.
да връща часовник подобен да показаният като трябва да бъде направен от "*" и да бъде обграден с "."
N винаги ще бъде нечетно число.
Примери:
Enter number: 5

.*****.
..***..
...*...
..***..
.*****.
Часовникът за N = 7 ще изглежда така:

*******
.*****.
..***..
...*...
..***..
.*****.
*******

"""


def sands_of_time():
    number = int(input('Enter your clock capacity: '))
    the_numbers = range(1, number + 1)
    counter = 0

    for i in the_numbers[::-1]:
        if i == 1:
            break
        if i % 2 != 0:
            counter += 1
            sand_amount = i
            if the_numbers[counter] < i:
                print(sand_amount * "*" + ".")
            else:
                print(sand_amount * "*")

    counter = 0

    for i in the_numbers:
        if i % 2 != 0:
            counter += 1
            sand_amount = i
            if the_numbers[counter] < i:
                print(sand_amount * "*" + ".")
            else:
                print(sand_amount * "*")

    return True


print(sands_of_time())
