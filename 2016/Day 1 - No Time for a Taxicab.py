'''
# Part 1

directions = []
pos = [0, 0]
facing = 0
moves = {0:(0, 1), 1:(1, 0), 2:(0, -1), 3:(-1, 0)}

with open('2016/data/day1.txt') as file:
    for line in file:
        directions += line.strip().split(", ")

for direction in directions:
    if direction[0] == "L":
        facing = (facing - 1) % 4
    elif direction[0] == "R":
        facing = (facing + 1) % 4
    for _ in range(int(direction[1:])):
        pos[0] += moves[facing][0]
        pos[1] += moves[facing][1]

print(abs(pos[0]) + abs(pos[1]))
'''

# Part 2

directions = []
pos = [0, 0]
facing = 0
moves = {0:(0, 1), 1:(1, 0), 2:(0, -1), 3:(-1, 0)}
visited = []
found = False

with open('2016/data/day1.txt') as file:
    for line in file:
        directions += line.strip().split(", ")

for direction in directions:
    if direction[0] == "L":
        facing = (facing - 1) % 4
    elif direction[0] == "R":
        facing = (facing + 1) % 4
    for _ in range(int(direction[1:])):
        pos[0] += moves[facing][0]
        pos[1] += moves[facing][1]
        if tuple(pos) in visited:
            found = True
            break
        visited.append(tuple(pos))
    if found:
        break

print(pos)
print(abs(pos[0]) + abs(pos[1]))