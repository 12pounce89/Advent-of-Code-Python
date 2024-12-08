# Part 1
'''
import math

steps = 0
current = "AAA"
order = ""
nodes = dict()

with open('data/day8.txt') as file:
    count = 0
    for line in file:
        count += 1
        if count == 1:
            order = line.strip()
        elif count >= 3:
            broken_line = line.split("=")
            nodes[broken_line[0].strip()] = [broken_line[1][2] + broken_line[1][3] + broken_line[1][4], broken_line[1][7] + broken_line[1][8] + broken_line[1][9]]

while True:
    if (current == "ZZZ"):
        break
    if (order[steps % len(order)] == "L"):
        current = nodes[current][0]
    else:
        current = nodes[current][1]
    steps += 1

print(steps)
'''

# Part 2

import math

steps = 0
current = "AAA"
order = ""
nodes = dict()

with open('data/day8.txt') as file:
    count = 0
    for line in file:
        count += 1
        if count == 1:
            order = line.strip()
        elif count >= 3:
            broken_line = line.split("=")
            nodes[broken_line[0].strip()] = [broken_line[1][2] + broken_line[1][3] + broken_line[1][4], broken_line[1][7] + broken_line[1][8] + broken_line[1][9]]

positions = []
for key in nodes:
    if key[2] == "A":
        positions.append(key)

finished = dict()
done = 0

while True:
    for item in positions:
        if item[2] == "Z":
            finished[item] = steps
            positions.remove(item)
    if done >= len(positions):
        break
    for i in range(len(positions)):
        if (positions[i] == "ZZZ"):
            break
        if (order[steps % len(order)] == "L"):
            positions[i] = nodes[positions[i]][0]
        else:
            positions[i] = nodes[positions[i]][1]
        steps += 1

distances = []
for key in finished:
    distances.append(finished[key])
print(distances)
lcm = distances[0]
for i in range(1, len(distances)):
    lcm = (lcm * distances[i] // math.gcd(lcm, distances[i]))

print(lcm)