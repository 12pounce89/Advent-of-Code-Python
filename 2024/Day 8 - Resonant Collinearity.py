'''
# Part 1

map = []
antinodes = []

with open('2024/data/day8.txt') as file:
    for line in file:
        map.append(list(line.strip()))
        antinodes.append(["." for i in range(len(line.strip()))])

nodes = dict()

for i, line in enumerate(map):
    for j, char in enumerate(line):
        if char != ".":
            if char not in nodes:
                nodes[char] = []
            nodes[char].append((i, j))

for key in nodes:
    for i, pos1 in enumerate(nodes[key]):
        for j in range(i + 1, len(nodes[key])):
            pos2 = nodes[key][j]
            newPos1 = []
            newPos2 = []
            if pos1[0] < pos2[0]:
                newPos1.append(2 * pos1[0] - pos2[0])
                newPos2.append(2 * pos2[0] - pos1[0])
            elif pos1[0] >= pos2[0]:
                newPos1.append(2 * pos1[0] - pos2[0])
                newPos2.append(2 * pos2[0] - pos1[0])
            newPos1.append(2 * pos1[1] - pos2[1])
            newPos2.append(2 * pos2[1] - pos1[1])
            if 0 <= newPos1[0] < len(antinodes) and 0 <= newPos1[1] < len(antinodes[0]):
                antinodes[newPos1[0]][newPos1[1]] = "#"
            if 0 <= newPos2[0] < len(antinodes) and 0 <= newPos2[1] < len(antinodes[0]):
                antinodes[newPos2[0]][newPos2[1]] = "#"

sum = 0

for line in antinodes:
    # print("".join(line))
    for char in line:
        if char == "#":
            sum += 1

print("\n", sum)
'''

# Part 2

map = []
antinodes = []

with open('2024/data/day8.txt') as file:
    for line in file:
        map.append(list(line.strip()))
        antinodes.append(["." for i in range(len(line.strip()))])

nodes = dict()

for i, line in enumerate(map):
    for j, char in enumerate(line):
        if char != ".":
            if char not in nodes:
                nodes[char] = []
            nodes[char].append((i, j))

for key in nodes:
    for i, pos in enumerate(nodes[key]):
        for j in range(i + 1, len(nodes[key])):
            pos1 = pos
            pos2 = nodes[key][j]
            change = (pos1[0] - pos2[0], pos1[1] - pos2[1])
            while True:
                newPos1 = (pos1[0] - change[0], pos1[1] - change[1])
                newPos2 = (pos2[0] + change[0], pos2[1] + change[1])
                if (newPos1[0] < 0 or newPos1[0] >= len(antinodes) or newPos1[1] < 0 or newPos1[1] >= len(antinodes[0])) and (newPos2[0] < 0 or newPos2[0] >= len(antinodes) or newPos2[1] < 0 or newPos2[1] >= len(antinodes[0])):
                    break
                if 0 <= newPos1[0] < len(antinodes) and 0 <= newPos1[1] < len(antinodes[0]):
                    antinodes[newPos1[0]][newPos1[1]] = "#"
                if 0 <= newPos2[0] < len(antinodes) and 0 <= newPos2[1] < len(antinodes[0]):
                    antinodes[newPos2[0]][newPos2[1]] = "#"
                pos1 = newPos1
                pos2 = newPos2

sum = 0

for line in antinodes:
    for char in line:
        if char == "#":
            sum += 1

print()
print(sum)