'''
# Part 1

floor = 0

with open('2015/data/day1.txt') as file:
    for line in file:
        for char in list(line.strip()):
            if char == "(":
                floor += 1
            elif char == ")":
                floor -= 1

print(floor)
'''

# Part 2

floor = 0
step = 0

with open('2015/data/day1.txt') as file:
    for line in file:
        for pos, char in enumerate(list(line.strip())):
            if char == "(":
                floor += 1
            elif char == ")":
                floor -= 1
            if floor < 0:
                step = pos + 1
                break

print(step)
