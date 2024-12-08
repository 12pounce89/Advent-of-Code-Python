'''
# Part 1

platform = []

with open('2023/data/day14.txt') as file:
    for line in file:
        platform.append(list(line.strip()))

for i in range(len(platform)):
    for j in range(len(platform[i])):
        pos = i
        if platform[i][j] == "O":
            while pos > 0 and platform[pos - 1][j] == ".":
                platform[pos][j] = "."
                platform[pos - 1][j] = "O"
                pos -= 1

load = 0
mult = len(platform)

for i in range(len(platform)):
    for char in platform[i]:
        if char == "O":
            load += mult
    mult -= 1

print(load)
'''

# Part 2

platform = []
pastStates = dict()

with open('2023/data/tester.txt') as file:
    for line in file:
        platform.append(list(line.strip()))

def roll_north(plat):
    for i in range(len(plat)):
        for j in range(len(plat[0])):
            pos = i
            # if j == 0:
            #     print(len(plat[i]), i)
            if plat[i][j] == "O":
                while pos > 0 and plat[pos - 1][j] == ".":
                    plat[pos][j] = "."
                    plat[pos - 1][j] = "O"
                    pos -= 1
    return plat

def roll_east(plat):
    for j in range(len(plat[0]) - 1, -1, -1):
        for i in range(len(plat)):
            pos = j
            if plat[i][j] == "O":
                while pos < len(plat[0]) - 1 and plat[i][pos + 1] == ".":
                    plat[i][pos] = "."
                    plat[i][pos + 1] = "O"
                    pos += 1
    return plat

def roll_south(plat):
    for i in range(len(plat) - 1, -1, -1):
        for j in range(len(plat[0])):
            pos = i
            if plat[i][j] == "O":
                while pos < len(plat) - 1 and plat[pos + 1][j] == ".":
                    plat[pos][j] = "."
                    plat[pos + 1][j] = "O"
                    pos += 1
    return plat

def roll_west(plat):
    for j in range(len(plat[0])):
        for i in range(len(plat)):
            pos = j
            if plat[i][j] == "O":
                while pos > 0 and plat[i][pos - 1] == ".":
                    plat[i][pos] = "."
                    plat[i][pos - 1] = "O"
                    pos -= 1
    return plat

cycle = 0
found = False
stringPlatform = ""

while cycle < 1000000000:
    cycle += 1
    print(cycle)
    if stringPlatform in pastStates and not found:
        pos = pastStates[stringPlatform]
        cycle = 1000000000 - (1000000000 - cycle) % (cycle - pastStates[stringPlatform])

    platform = roll_north(platform)
    platform = roll_west(platform)
    platform = roll_south(platform)
    platform = roll_east(platform)

    stringPlatform = ""
    for line in platform:
        for char in line:
            stringPlatform += char

    pastStates[stringPlatform] = cycle

load = 0
mult = len(platform)

for i in range(len(platform)):
    for char in platform[i]:
        if char == "O":
            load += mult
    mult -= 1

print(load)

# for line in platform:
#     for char in line:
#         print(char, end="")
#     print()

platform = roll_north(platform)

load = 0
mult = len(platform)

for i in range(len(platform)):
    for char in platform[i]:
        if char == "O":
            load += mult
    mult -= 1

print(load)

platform = roll_west(platform)

load = 0
mult = len(platform)

for i in range(len(platform)):
    for char in platform[i]:
        if char == "O":
            load += mult
    mult -= 1

print(load)

platform = roll_south(platform)

load = 0
mult = len(platform)


for i in range(len(platform)):
    for char in platform[i]:
        if char == "O":
            load += mult
    mult -= 1

print(load)

platform = roll_east(platform)

load = 0
mult = len(platform)


for i in range(len(platform)):
    for char in platform[i]:
        if char == "O":
            load += mult
    mult -= 1

print(load)

platform = roll_north(platform)

load = 0
mult = len(platform)

for i in range(len(platform)):
    for char in platform[i]:
        if char == "O":
            load += mult
    mult -= 1

print(load)

platform = roll_west(platform)

load = 0
mult = len(platform)

for i in range(len(platform)):
    for char in platform[i]:
        if char == "O":
            load += mult
    mult -= 1

print(load)

platform = roll_south(platform)

load = 0
mult = len(platform)


for i in range(len(platform)):
    for char in platform[i]:
        if char == "O":
            load += mult
    mult -= 1

print(load)

platform = roll_east(platform)

load = 0
mult = len(platform)


for i in range(len(platform)):
    for char in platform[i]:
        if char == "O":
            load += mult
    mult -= 1

print(load)

platform = roll_north(platform)

load = 0
mult = len(platform)

for i in range(len(platform)):
    for char in platform[i]:
        if char == "O":
            load += mult
    mult -= 1

print(load)

platform = roll_west(platform)

load = 0
mult = len(platform)

for i in range(len(platform)):
    for char in platform[i]:
        if char == "O":
            load += mult
    mult -= 1

print(load)

platform = roll_south(platform)

load = 0
mult = len(platform)


for i in range(len(platform)):
    for char in platform[i]:
        if char == "O":
            load += mult
    mult -= 1

print(load)

platform = roll_east(platform)

load = 0
mult = len(platform)


for i in range(len(platform)):
    for char in platform[i]:
        if char == "O":
            load += mult
    mult -= 1

print(load)
