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
    visited.add(str(pos[0]) + str(pos[1]))

print(len(visited))