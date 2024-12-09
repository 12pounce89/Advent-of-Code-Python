'''
# Part 1

target = 0

with open('2015/data/day20.txt') as file:
    for line in file:
        target = int(str(target) + line.strip())

house = 1
presents = 10

while presents < target:
    house += 1
    total = 0
    sqrt = int(house**0.5)
    for i in range(1, sqrt + 1):
        if house % i == 0:
            total += i
            if i != house // i:
                total += house // i
    presents = 10 * total

print(house)
'''

# Part 2

target = 0

with open('2015/data/day20.txt') as file:
    for line in file:
        target = int(str(target) + line.strip())

elves = dict()
house = 0
presents = 0

while presents < target:
    house += 1
    elves[house] = 0
    total = 0
    sqrt = int(house**0.5)
    for i in range(1, sqrt + 1):
        if house % i == 0:
            if elves[i] < 50:
                total += i
                elves[i] += 1
            if i != house // i:
                if elves[house // i] < 50:
                    total += house // i
                    elves[house // i] += 1
    presents = 11 * total

print(house)