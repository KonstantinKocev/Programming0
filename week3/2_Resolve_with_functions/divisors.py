def divisors(number):
	start, small_n, divisor = 1, number - 1, []

	while start <= small_n:
		if number % start == 0:
			divisor += [start]

		start += 1
	return divisor


print(divisors(20))
