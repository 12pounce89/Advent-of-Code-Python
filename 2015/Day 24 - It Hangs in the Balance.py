'''
# Part 1

import itertools

gifts = []
weight = 0

with open('2015/data/day24.txt') as file:
    for line in file:
        weight += int(line.strip())
        gifts.append(int(line.strip()))

target = int(weight / 3)
gifts = sorted(gifts, reverse=True)
minQuantum = -1

for i in range(1, len(gifts) + 1):
    combinations = itertools.combinations(gifts, i)
    for combo in combinations:
        if sum(combo) == target:
            quantum = 1
            for num in combo:
                quantum *= num
            if minQuantum == -1:
                minQuantum = quantum
            elif quantum < minQuantum:
                minQuantum = quantum
    if minQuantum != -1:
        break

print(minQuantum)
'''

# Part 2

import itertools

gifts = []
weight = 0

with open('2015/data/day24.txt') as file:
    for line in file:
        weight += int(line.strip())
        gifts.append(int(line.strip()))

target = int(weight / 4)
gifts = sorted(gifts, reverse=True)
minQuantum = -1

for i in range(1, len(gifts) + 1):
    combinations = itertools.combinations(gifts, i)
    for combo in combinations:
        if sum(combo) == target:
            quantum = 1
            for num in combo:
                quantum *= num
            if minQuantum == -1:
                minQuantum = quantum
            elif quantum < minQuantum:
                minQuantum = quantum
    if minQuantum != -1:
        break

print(minQuantum)