"""Най-голямото и най-малкото число от цифри.
Във файла large_and_small.py напишете програма, която:

Чете едно цяло число n от потребителя
На екрана извежда най-голямото число, което може да се получи със същите цифри от n
На екрана извежда най-малкото число, което може да се получи със същите цифри от n
n може да е произволно голямо число, като направете решение за число, в което няма да цифрата 0.

Примери:

Enter n: 12311984324
Largest: 98443322111
Smallest: 11122334489

"""

def large_small(n):
	a = n % 10
	n = n // 10

	b = n % 10
	n = n // 10

	c = n % 10
	n = n // 10

	largest = a

	if b >= a and b >= c:
		largest = b
	if c >= a and c >= b:
		largest = c

	smallest = a

	if b <= a and b <= c:
		smallest = b
	if c <= a and c <= b:
		smallest = c

	middle = c

	if (largest == c and smallest == b) or (largest == b and smallest == c):
		middle = a
	elif (largest == a and smallest == c) or (largest == c and smallest == a):
		middle = b

	smallest_num = smallest * 100 + middle * 10 + largest
	max_num = largest * 100 + middle * 10 + smallest

	return smallest_num, max_num


print(large_small(192))