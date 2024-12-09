# Part 1

import re

changes = dict()
molecule = []
last = False

with open('2015/data/day19.txt') as file:
    for line in file:
        if last:
            molecule = re.findall('[A-Z][a-z]*', line.strip())
        elif line.strip() == "":
            last = True
        else:
            broken = line.strip().split(" => ")
            if broken[0] not in changes:
                changes[broken[0]] = []
            changes[broken[0]].append(broken[1])

new = set()

for key in changes:
    for i in range(len(molecule)):
        if molecule[i] == key:
            for change in changes[key]:
                molecule[i] = change
                new.add("".join(molecule))
                molecule[i] = key

print(len(new))