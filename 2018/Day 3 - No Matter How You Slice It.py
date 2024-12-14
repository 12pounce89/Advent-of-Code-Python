'''
# Part 1

import re

plans = []

with open('2018/data/day3.txt') as file:
    for line in file:
        plans.append(re.findall('\d+', line.strip()))

coords = {}

for plan in plans:
    for i in range(int(plan[1]), int(plan[1]) + int(plan[3])):
        for j in range(int(plan[2]), int(plan[2]) + int(plan[4])):
            if (i, j) not in coords:
                coords[(i, j)] = 0
            coords[(i, j)] += 1

overage = 0

for key in coords:
    if coords[key] > 1:
        overage += 1

print(overage)
'''

# Part 2

import re

plans = []

with open('2018/data/day3.txt') as file:
    for line in file:
        plans.append(re.findall('\d+', line.strip()))

coords = {}

for plan in plans:
    for i in range(int(plan[1]), int(plan[1]) + int(plan[3])):
        for j in range(int(plan[2]), int(plan[2]) + int(plan[4])):
            if (i, j) not in coords:
                coords[(i, j)] = 0
            coords[(i, j)] += 1

for plan in plans:
    failed = False
    for i in range(int(plan[1]), int(plan[1]) + int(plan[3])):
        for j in range(int(plan[2]), int(plan[2]) + int(plan[4])):
            if coords[(i, j)] > 1:
                failed = True
                break
        if failed:
            break
    if not failed:
        print(plan[0])
        break
