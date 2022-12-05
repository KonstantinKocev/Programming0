"""Задача 9 - Имена, подредени по азбучен ред.
Във файл sorted_names.py, напишете програма, която:

Чете едно число n от потребителя
На следващите n реда чете по 1 име от потребителя (string)
Накрая, програмата отпечатва всички въведени имена, подредени по азбучен ред в нарастващ ред (от a нагоре)
Може да разгледате какво прави функцията sorted в Python. Работи над списъци.

Примери:

Enter n: 5
Rado
Ivo
Maria
Lora
Anna
Sorted names are:
Anna
Ivo
Lora
Maria
Rado

"""

n = int(input('Enetr count of names: '))

n_count = 1
names = []

while n_count <= n:
    name = input('Enter name:')
    names = names + [name]
    n_count += 1

names = sorted(names)

for name in names:
    print(name)
