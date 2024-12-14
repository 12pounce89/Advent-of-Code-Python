'''
# Part 1

polymer = ""

with open('2018/data/day5.txt') as file:
    for line in file:
        polymer += line.strip()

polymer = list(polymer)
changed = True

while changed:
    changed = False
    i = 0
    while i < len(polymer) - 1:
        if (polymer[i].upper() == polymer[i] and polymer[i + 1] == polymer[i].lower()) or (polymer[i].lower() == polymer[i] and polymer[i + 1] == polymer[i].upper()):
            polymer.pop(i)
            polymer.pop(i)
            i -= 1
            changed = True
        i += 1

print(len(polymer))
'''

# Part 2

originalPolymer = ""

with open('2018/data/day5.txt') as file:
    for line in file:
        originalPolymer += line.strip()

letters = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

for key in letters:
    polymer = list(originalPolymer)
    i = 0
    changed = True
    while i < len(polymer):
        if polymer[i].lower() == key:
            polymer.pop(i)
            i -= 1
        i += 1
    while changed:
        changed = False
        i = 0
        while i < len(polymer) - 1:
            if (polymer[i].upper() == polymer[i] and polymer[i + 1] == polymer[i].lower()) or (polymer[i].lower() == polymer[i] and polymer[i + 1] == polymer[i].upper()):
                polymer.pop(i)
                polymer.pop(i)
                i -= 2
                changed = True
            i += 1
    letters[key] = len(polymer)

min = -1

for key in letters:
    if letters[key] < min or min == -1:
        min = letters[key]

print(min)