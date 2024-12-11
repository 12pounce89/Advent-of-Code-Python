'''
# Part 1

directions = []

with open('2017/data/day5.txt') as file:
    for line in file:
        directions.append(int(line.strip()))

pos = 0
steps = 0

while 0 <= pos < len(directions):
    directions[pos] += 1
    pos += directions[pos] - 1
    steps += 1

print(steps)
'''

# Part 2

directions = []

with open('2017/data/day5.txt') as file:
    for line in file:
        directions.append(int(line.strip()))

pos = 0
steps = 0

while 0 <= pos < len(directions):
    move = directions[pos]
    if directions[pos] >= 3:
        directions[pos] -= 1
    else:
        directions[pos] += 1
    pos += move
    steps += 1

print(steps)