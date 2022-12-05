from random import randint

n = int(input('Enter number: '))
num = randint(1, n)
print(num)
numbers = range(1, num)
for number in numbers:
    print(number + 1)
