# Part 1

import sys

sys.setrecursionlimit(9999999)
grid = []
grid2 = []
moves = {0:(-1, 0), 1:(0, 1), 2:(1, 0), 3:(0, -1)}

with open('2024/data/day16.txt') as file:
    for line in file:
        grid.append(list(line.strip()))
        grid2.append(list(line.strip()))

found = False
finishedPoints = set()

for i, line in enumerate(grid):
    for j, char in enumerate(line):
        if char == "S":
            start = (i, j)
            found = True
            break
    if found:
        break

def move(pos, visited=set(), facing=1, points=0):
    visited.add(pos)
    if len(finishedPoints) > 0:
        if points > min(finishedPoints):
            return
    # print(visited)
    y, x = pos
    a, b = moves[facing]
    c, d = moves[(facing + 1) % 4]
    e, f = moves[(facing - 1) % 4]

    if (y + a, x + b) in visited:
        pass
    elif grid[y + a][x + b] == "E":
        finishedPoints.add(points + 1)
    elif grid[y + a][x + b] == ".":
        move((y + a, x + b), visited, facing, points + 1)
        visited.remove((y + a, x + b))

    if (y + c, x + d) in visited:
        pass
    elif grid[y + c][x + d] == "E":
        finishedPoints.add(points + 1001)
    elif grid[y + c][x + d] == ".":
        move((y + c, x + d), visited, (facing + 1) % 4, points + 1001)
        visited.remove((y + c, x + d))

    if (y + e, x + f) in visited:
        pass
    elif grid[y + e][x + f] == "E":
        finishedPoints.add(points + 1001)
    elif grid[y + e][x + f] == ".":
        move((y + e, x + f), visited, (facing - 1) % 4, points + 1001)
        visited.remove((y + e, x + f))

move(start)

# print(sorted(list(finishedPoints)))
print(min(finishedPoints))