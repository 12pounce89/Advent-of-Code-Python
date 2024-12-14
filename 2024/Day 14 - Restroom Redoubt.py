'''
# Part 1

import re

positions = []
velocities = []

with open('2024/data/day14.txt') as file:
    for line in file:
        nums = re.findall('-?\d+', line.strip())
        nums = [int(x) for x in nums]
        positions.append(nums[:2])
        velocities.append(nums[2:])

for _ in range(100):
    for pos in range(len(positions)):
        positions[pos][0] = (positions[pos][0] + velocities[pos][0]) % 101
        positions[pos][1] = (positions[pos][1] + velocities[pos][1]) % 103

quads = [0, 0, 0, 0]

for item in positions:
    if item[0] < 50:
        if item[1] < 51:
            quads[0] += 1
        elif item[1] > 51:
            quads[2] += 1
    elif item[0] > 50:
        if item[1] < 51:
            quads[1] += 1
        elif item[1] > 51:
            quads[3] += 1

product = 1

for item in quads:
    product *= item

print(product)
'''

# Part 2

import re

positions = []
velocities = []
seconds = 0

with open('2024/data/day14.txt') as file:
    for line in file:
        nums = re.findall('-?\d+', line.strip())
        nums = [int(x) for x in nums]
        positions.append(nums[:2])
        velocities.append(nums[2:])

found = False

while True:
    checkPos = set()
    for pos in positions:
        checkPos.add(tuple(pos))
    if len(checkPos) == len(positions):
        for i in range(103):
            for j in range(71):
                coords = [[j + x, i] for x in range(31)]
                for item in coords:
                    if item in positions and item == coords[-1]:
                        found = True
                    if item not in positions:
                        break
            if found:
                break
    if found:
        break
    seconds += 1
    for pos in range(len(positions)):
        positions[pos][0] = (positions[pos][0] + velocities[pos][0]) % 101
        positions[pos][1] = (positions[pos][1] + velocities[pos][1]) % 103

print(seconds)