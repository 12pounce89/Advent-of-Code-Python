'''
# Part 1

import itertools

containers = []

with open('2015/data/day17.txt') as file:
    for line in file:
        containers.append(int(line.strip()))

containers = sorted(containers, reverse=True)
target = 150
options = 0

for i in range(1, len(containers) + 1):
    combinations = itertools.combinations(containers, i)
    for combo in combinations:
        if int(sum(combo)) == target:
            options += 1

print(options)
'''

# Part 2

import itertools

containers = []

with open('2015/data/day17.txt') as file:
    for line in file:
        containers.append(int(line.strip()))

containers = sorted(containers, reverse=True)
target = 150
options = 0

for i in range(1, len(containers) + 1):
    combinations = itertools.combinations(containers, i)
    for combo in combinations:
        if int(sum(combo)) == target:
            options += 1
    if options > 0:
        break

print(options)