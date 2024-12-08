'''
# Part 1

myFile = []

with open('2015/data/day5.txt') as file:
    for line in file:
        myFile.append(list(line.strip()))

nice = 0

for line in myFile:
    vowels = 0
    double = False
    allowed = True
    if line[0] in ['a', 'e', 'i', 'o', 'u']:
        vowels += 1
    for i in range(len(line) - 1):
        if line[i + 1] in ['a', 'e', 'i', 'o', 'u']:
            vowels += 1
        if line[i] == line[i + 1]:
            double = True
        if line[i] + line[i + 1] in ['ab', 'cd', 'pq', 'xy']:
            allowed = False
    if vowels >= 3 and double and allowed:
        nice += 1

print(nice)
'''

# Part 2

myFile = []

with open('2015/data/day5.txt') as file:
    for line in file:
        myFile.append(line.strip())

nice = 0

for line in myFile:
    spaced = False
    doublePair = False # 110
    for i in range(len(line) - 2):
        if line[i] == line[i + 2]:
            spaced = True
    pairs = set()
    count = 0
    for i in range(len(line) - 3):
        if (line[i] + line[i + 1]) in line[i + 2:]:
            doublePair = True
            break
    if spaced and doublePair:
        nice += 1

print(nice)