'''
# Part 1

directions = ""

with open('2015/data/day3.txt') as file:
    for line in file:
        directions += line.strip()

pos = [0, 0]
visited = {str(pos[0]) + str(pos[1])}
moves = {"v":(0, -1), "^":(0, 1), "<":(-1, 0), ">":(1, 0)}

for char in directions:
    pos[0] += moves[char][0]
    pos[1] += moves[char][1]
    visited.add(str(pos[0]) + ":" + str(pos[1]))

print(len(visited))
'''

# Part 2

directions = ""

with open('2015/data/day3.txt') as file:
    for line in file:
        directions += line.strip()

pos1 = [0, 0]
pos2 = [0, 0]
visited = {str(pos1[0]) + ":" + str(pos1[1])}
moves = {"v":(0, -1), "^":(0, 1), "<":(-1, 0), ">":(1, 0)}

for i, char in enumerate(directions):
    if i % 2 == 0:
        pos1[0] += moves[char][0]
        pos1[1] += moves[char][1]
        visited.add(str(pos1[0]) + ":" + str(pos1[1]))
    else:
        pos2[0] += moves[char][0]
        pos2[1] += moves[char][1]
        visited.add(str(pos2[0]) + ":" + str(pos2[1]))

print(len(visited))