first_name = input('Enter your first name please:')
second_name = input('Enter your second name please: ')
third_name = input('Enter your third name please: ')

def person(a, b, c, d):
	birth_year = int(input('Enter birth year please: '))
	current_year = 2023
	current_age = 0
	current_age = current_year - birth_year

	return first_name, second_name, third_name, current_age

print(person())
