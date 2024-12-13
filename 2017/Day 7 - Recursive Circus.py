'''
# Part 1

allPrograms = set()
above = set()

with open('2017/data/day7.txt') as file:
    for line in file:
        broken = line.strip().split(" -> ")
        if len(broken) > 1:
            upper = broken[1].split(", ")
            for item in upper:
                above.add(item)
        programs.add(broken[0].split(" ")[0])

for item in programs:
    if item not in above:
        print(item)
        break
'''

# Part 2

programs = {}
weights = {}
allPrograms = set()
above = set()
fixed = 0

def get_weight(program):
    global fixed
    # print('test')
    # print(fixed, 'found')
    totalWeight = weights[program]
    if program in programs:
        towers = {}
        towers2 = {}
        for item in programs[program]:
            aboveWeight, aboveTower = get_weight(item)
            if aboveWeight not in towers:
                # if len(towers) == 0:
                    # print('test')
                towers[aboveWeight] = 0
                towers2[aboveWeight] = []
                # else:
                #     problem.append(aboveTower)
                #     for key in towers:
                #         problem.append(key)
                #         aboveWeight = key
            towers[aboveWeight] += 1
            towers2[aboveWeight].append(aboveTower)
        if len(towers) > 1:
            print(program, towers)
            for key in towers:
                if towers[key] > 1:
                    totalWeight += key * towers[key]
                    proper = key
                if towers[key] == 1:
                    wrong = key
            # print(aboveTower, weights[aboveTower], wrong, proper, (wrong - proper))
            fixed = weights[towers2[wrong][0]] - (wrong - proper)
        else:
            for key in towers:
                proper = key
        totalWeight += proper * (towers[proper] + 1)
    return totalWeight, program

with open('2017/data/day7.txt') as file:
    for line in file:
        broken = line.strip().split(") -> ")
        weights[broken[0].split()[0]] = int(broken[0].split(" (")[1].split(")")[0])
        if len(broken) > 1:
            base = broken[0].split()[0]
            programs[base] = []
            upper = broken[1].split(", ")
            for item in upper:
                programs[base].append(item)
                above.add(item)
        allPrograms.add(broken[0].split(" ")[0])

for item in programs:
    if item not in above:
        base = item
        break

get_weight(base)

print(fixed)
# print(problem)
# print(weights[problem[0]] - problem[1])