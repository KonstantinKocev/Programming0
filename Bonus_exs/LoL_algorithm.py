"""Pick a champion!

Write a program that picks a champion for you in league
Input:
Enemy team:
How many tanks?
How many damage dealers?
  - how many of these are assassins?
How many healers?

Allied team:
How many tanks?
How many damage dealers?
  - how many of these are assassins?
How many healers?

Example:

Enemy:
Tanks 3
Damage dealers 1
  - 1 assassin
Healers 1

Allied:
Tanks 1
Damage dealers 1
Healers 2

Solved! Pick one of these: Tristana, Kindred, Master Yi, Garen

"""

tanks = ['Orn', 'Shen', 'Nasus', 'Ramus']

dmg_dealers = ['Zed', 'Sindra', 'Lux', 'LeBlanc']

healers = ['Soraka', 'Nami', 'Sona', 'Yummi']

start = 1

while start <= 4:
    allied_champs = input('Enter allied champion please: ')


    start += 1