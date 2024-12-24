'''
# Part 1

gates = {}
initializing = True
skipped = []

with open('2024/data/day24.txt') as file:
    for line in file:
        if line.strip() == "":
            initializing = False
        elif initializing:
            broken = line.strip().split(': ')
            if broken[0] not in gates:
                gates[broken[0]] = None
            if broken[1] == '0':
                gates[broken[0]] = False
            elif broken[1] == '1':
                gates[broken[0]] = True
        else:
            broken = line.strip().split(' -> ')
            start = broken[0].split()
            if start[0] not in gates or start[2] not in gates:
                skipped.append(line.strip())
                continue
            if broken[1] not in gates:
                gates[broken[1]] = None
            if start[1] == 'OR':
                if gates[start[0]] or gates[start[2]]:
                    gates[broken[1]] = True
                else:
                    gates[broken[1]] = False
            elif start[1] == 'AND':
                if gates[start[0]] and gates[start[2]]:
                    gates[broken[1]] = True
                else:
                    gates[broken[1]] = False
            elif start[1] == 'XOR':
                if (gates[start[0]] or gates[start[2]]) and not (gates[start[0]] and gates[start[2]]):
                    gates[broken[1]] = True
                else:
                    gates[broken[1]] = False


while len(skipped) > 0:
    newSkipped = []
    for line in skipped:
        broken = line.split(' -> ')
        start = broken[0].split()
        if start[0] not in gates or start[2] not in gates:
            newSkipped.append(line.strip())
            continue
        if broken[1] not in gates:
            gates[broken[1]] = None
        if start[1] == 'OR':
            if gates[start[0]] or gates[start[2]]:
                gates[broken[1]] = True
            else:
                gates[broken[1]] = False
        elif start[1] == 'AND':
            if gates[start[0]] and gates[start[2]]:
                gates[broken[1]] = True
            else:
                gates[broken[1]] = False
        elif start[1] == 'XOR':
            if (gates[start[0]] or gates[start[2]]) and not (gates[start[0]] and gates[start[2]]):
                gates[broken[1]] = True
            else:
                gates[broken[1]] = False
    skipped = newSkipped[:]

weakest = {}

for key in gates:
    if key[0] == 'z':
        weakest[key] = gates[key]

n = 1
val = 0

for key in weakest:
    if weakest[key]:
        val += n
    n *= 2

print(val)
'''

# Part 2

gates = {}
initializing = True
skipped = []

with open('2024/data/day24.txt') as file:
    for line in file:
        if line.strip() == "":
            initializing = False
        elif initializing:
            broken = line.strip().split(': ')
            if broken[0] not in gates:
                gates[broken[0]] = None
            if broken[1] == '0':
                gates[broken[0]] = False
            elif broken[1] == '1':
                gates[broken[0]] = True
        else:
            broken = line.strip().split(' -> ')
            start = broken[0].split()
            if start[0] not in gates or start[2] not in gates:
                skipped.append(line.strip())
                continue
            if broken[1] not in gates:
                gates[broken[1]] = None
            if start[1] == 'OR':
                if gates[start[0]] or gates[start[2]]:
                    gates[broken[1]] = True
                else:
                    gates[broken[1]] = False
            elif start[1] == 'AND':
                if gates[start[0]] and gates[start[2]]:
                    gates[broken[1]] = True
                else:
                    gates[broken[1]] = False
            elif start[1] == 'XOR':
                if (gates[start[0]] or gates[start[2]]) and not (gates[start[0]] and gates[start[2]]):
                    gates[broken[1]] = True
                else:
                    gates[broken[1]] = False


while len(skipped) > 0:
    newSkipped = []
    for line in skipped:
        broken = line.split(' -> ')
        start = broken[0].split()
        if start[0] not in gates or start[2] not in gates:
            newSkipped.append(line.strip())
            continue
        if broken[1] not in gates:
            gates[broken[1]] = None
        if start[1] == 'OR':
            if gates[start[0]] or gates[start[2]]:
                gates[broken[1]] = True
            else:
                gates[broken[1]] = False
        elif start[1] == 'AND':
            if gates[start[0]] and gates[start[2]]:
                gates[broken[1]] = True
            else:
                gates[broken[1]] = False
        elif start[1] == 'XOR':
            if (gates[start[0]] or gates[start[2]]) and not (gates[start[0]] and gates[start[2]]):
                gates[broken[1]] = True
            else:
                gates[broken[1]] = False
    skipped = newSkipped[:]

weakest = {}

for key in gates:
    if key[0] == 'z':
        weakest[key] = gates[key]

n = 1
val = 0

for key in weakest:
    if weakest[key]:
        val += n
    n *= 2

print(val)