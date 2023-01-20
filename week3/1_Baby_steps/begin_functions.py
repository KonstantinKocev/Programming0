# Square number.

def square(a):
	return a * a

print(square(5), '| Square')


# Factoriel.

def fact(a):
	start = 1

	total_num = 1

	while start <= a:
		total_num *= start

		start += 1
	return total_num

print(fact(5), '| Factoriel')


# Count elements.

def count_elements(items):
	counter = 1

	while counter <= len(items):
		counter += 1

	return counter - 1

print(count_elements(list(range(10))), '| Count elements')


# Is in list.

def member(x, xs):
	if x in xs:
		return 'True'
	else:
		return 'Fasle'

print(member('Python', ['Python', 'Haskel', 'Ruby']), '| Is in list')


# Grades that pass.

def grades_that_pass(students, grades, limit):
	counter = 0
	result = []

	for grade in grades:
		student = students[counter]
		if grade >= limit:
			result += [student]

		counter += 1

	return result


print(grades_that_pass(["Rado", "Ivo", "Maria", "Nina"], [3, 4.5, 5.5, 6], 4.0), '| Grades that pass')
