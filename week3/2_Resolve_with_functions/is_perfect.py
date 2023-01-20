def sum_ints(n):
	sum_nums = 0
	for i in n:
		sum_nums += i
	return sum_nums

def is_perfect(n):
	start = 1
	small_n = n - 1
	divisors = []

	while start <= small_n:
		if n % start == 0:
			divisors += [start]

		start += 1
	return sum_ints(divisors)

n = int(input('Enter number: '))

if is_perfect(n) == n:
	print(is_perfect(n), '| Is perfect!')
else:
	print(is_perfect(n), '| Is not perfect!')
