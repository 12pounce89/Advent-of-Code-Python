'''
# Part 1

import re

reindeer = []
distances = []

with open('2015/data/day14.txt') as file:
    for line in file:
        reindeer.append(re.findall("\d+", line.strip()))

for deer in reindeer:
    time = int(deer[1]) + int(deer[2])
    distance = (2503 // time) * int(deer[0]) * int(deer[1])
    if int(deer[1]) < (2503 % time):
        distance += int(deer[1]) * int(deer[0])
    else:
        distance += (2503 % time) * int(deer[0])
    distances.append(distance)

print(max(distances))
'''

# Part 2

import re

reindeer = []
distances = []

with open('2015/data/day14.txt') as file:
    for line in file:
        reindeer.append(re.findall("\d+", line.strip()) + [0, 0])

for i in range(2503):
    distances = []
    for j, deer in enumerate(reindeer):
        if 0 <= i % (int(deer[1]) + int(deer[2])) < int(deer[1]):
            deer[3] += int(deer[0])
        distances.append((j, deer[3]))
    winners = {distances[0][0]}
    greatest = distances[0][1]
    for item in distances[1:]:
        if item[1] > greatest:
            winners = set()
            winners.add(int(item[0]))
            greatest = item[1]
        elif item[1] == greatest:
            winners.add(int(item[0]))
    # print(winners)
    for item in winners:
        reindeer[item][4] += 1

most = 0
for deer in reindeer:
    if deer[4] > most:
        most = deer[4]

print(most)