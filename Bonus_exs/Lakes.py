n = input('Enter your letters: ')

d = 500
h = 1000
u = 500

sum_square_d = []
sum_square_h = []
sum_square_u = []


for square in n:
	if square == 'd':
		sum_square_d += [d]
	if square == 'h':
		sum_square_h += [h]
	if square == 'u':
		sum_square_u += [u]


if len(sum_square_d) >= 2:
	sum_square_d += [1000 * (len(sum_square_d) - 1)]

if len(sum_square_u) >= 2:
	sum_square_u += [1000 * (len(sum_square_u) - 1)]


total_litters = sum(sum_square_d) + (sum(sum_square_h) * (len(sum_square_d) - 1)) + sum(sum_square_u)

print(total_litters)
