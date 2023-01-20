def divisors(n):
	start, small_n, divisors = 1, n - 1, []

	while start <= small_n:
		if n % start == 0:
			divisors += [start]

		start += 1
	return divisors


print(divisors(20))
