def divisors(n):
    start, small_n, divisors = 1, n - 1, []

    while start <= small_n:
        if n % start == 0:
            divisors += [start]

        start += 1
    return divisors


def sum_ints(n):
    sum_num = 0
    for i in n:
        sum_num += i
    return sum_num


print(sum_ints(divisors(20)), '| Sum divisors')
