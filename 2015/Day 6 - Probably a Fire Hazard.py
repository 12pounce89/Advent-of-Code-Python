'''
# Part 1

directions = []

with open('2015/data/day6.txt') as file:
    for line in file:
        broken = line.strip().split()
        if broken[0] == "toggle":
            start = broken[1].split(",")
            start = (int(start[0]), int(start[1]))
            stop = broken[3].split(",")
            stop = (int(stop[0]), int(stop[1]))
            directions.append([broken[0], start, stop])
        elif broken[0] == "turn":
            start = broken[2].split(",")
            start = (int(start[0]), int(start[1]))
            stop = broken[4].split(",")
            stop = (int(stop[0]), int(stop[1]))
            directions.append([broken[1], start, stop])

lights = [[0 for i in range(1000)] for j in range(1000)]

for line in directions:
    if line[0] == "on":
        for i in range(line[1][1], line[2][1] + 1):
            for j in range(line[1][0], line[2][0] + 1):
                lights[i][j] = 1
    elif line[0] == "off":
        for i in range(line[1][1], line[2][1] + 1):
            for j in range(line[1][0], line[2][0] + 1):
                lights[i][j] = 0
    elif line[0] == "toggle":
        for i in range(line[1][1], line[2][1] + 1):
            for j in range(line[1][0], line[2][0] + 1):
                lights[i][j] = (lights[i][j] + 1) % 2

count = 0

for line in lights:
    for char in line:
        if char == 1:
            count += 1

print(count)
'''

# Part 2

directions = []

with open('2015/data/day6.txt') as file:
    for line in file:
        broken = line.strip().split()
        if broken[0] == "toggle":
            start = broken[1].split(",")
            start = (int(start[0]), int(start[1]))
            stop = broken[3].split(",")
            stop = (int(stop[0]), int(stop[1]))
            directions.append([broken[0], start, stop])
        elif broken[0] == "turn":
            start = broken[2].split(",")
            start = (int(start[0]), int(start[1]))
            stop = broken[4].split(",")
            stop = (int(stop[0]), int(stop[1]))
            directions.append([broken[1], start, stop])

lights = [[0 for i in range(1000)] for j in range(1000)]

for line in directions:
    if line[0] == "on":
        for i in range(line[1][1], line[2][1] + 1):
            for j in range(line[1][0], line[2][0] + 1):
                lights[i][j] += 1
    elif line[0] == "off":
        for i in range(line[1][1], line[2][1] + 1):
            for j in range(line[1][0], line[2][0] + 1):
                if lights[i][j] > 0:
                    lights[i][j] -= 1
    elif line[0] == "toggle":
        for i in range(line[1][1], line[2][1] + 1):
            for j in range(line[1][0], line[2][0] + 1):
                lights[i][j] += 2

brightness = 0

for line in lights:
    for char in line:
        brightness += char

print(brightness)