n = list(input('Enter your string please: '))

vowels  = "aeiouyAEIOUY"
counter = 0
vowels_list = []

for i in n:
    if i in vowels:
        vowels_list += [i]
        counter += 1

print(vowels_list, [counter])