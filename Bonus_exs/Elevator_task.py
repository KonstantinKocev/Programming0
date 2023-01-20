people_count = int(input('Enter count of people: '))

counter = 1
people_weights = []

while counter <= people_count:
    people_kilograms = int(input('Enter kilograms for each person: '))
    people_weights += [people_kilograms]

    counter += 1


floors = int(input('Enter count of floors: '))

counter_2 = 1
floors_numbers = []

while counter_2 <= floors:
    number_of_floor = int(input('Enter number of floor: '))
    floors_numbers += [number_of_floor]

    counter_2 += 1


print('\nThe kilograms of each person: ', people_weights)
print('\nThe number of each floor: ', floors_numbers)


max_ppl = 2
max_kg = 250
elevator_weight = []
trips = 0

for i in people_weights:
    elevator_weight += [i]
    if sum(elevator_weight) <= max_kg:
        if len(elevator_weight) <= max_ppl:
            trips += 1
    else:
        trips += 1

print('\nThe count of trips are: ', trips)
