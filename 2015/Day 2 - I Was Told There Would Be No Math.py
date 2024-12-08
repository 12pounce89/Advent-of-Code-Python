'''
# Part 1

myFile = []

with open('2015/data/day2.txt') as file:
    for line in file:
        myFile.append(line.strip().split("x"))

sum = 0

for line in myFile:
    sides = [int(line[0]) * int(line[1]), int(line[0]) * int(line[2]), int(line[1]) * int(line[2])]
    sum += 2 * (sides[0] + sides[1] + sides[2]) + min(sides)

print(sum)
'''

# Part 2

myFile = []

with open('2015/data/day2.txt') as file:
    for line in file:
        myFile.append([int(x) for x in line.strip().split("x")])

sum = 0

for line in myFile:
    # sides = [int(line[0]) * int(line[1]), int(line[0]) * int(line[2]), int(line[1]) * int(line[2])]
    # sum += 2 * (sides[0] + sides[1] + sides[2]) + min(sides)
    sum += line[0] * line[1] * line[2]
    line.pop(0 if line[0] == max(line) else (1 if line[1] == max(line) else 2))
    sum += 2 * (line[0] + line[1]) 

print(sum)