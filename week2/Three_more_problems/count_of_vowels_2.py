n = list(input('Enter your string please: '))

vowels  = ["aeiouyAEIOUY"]
counter = 1
vow_total = 0

for i in n:
    if i in vowels:
        print(i)
        counter += 1
        vow_total += counter

print(vow_total)