# Part 1

steps = set()
limits = {}

with open('2018/data/tester.txt') as file:
    for line in file:
        broken = line.strip().split()
        steps.add(broken[1])
        steps.add(broken[7])
        if broken[1] not in limits:
            limits[broken[1]] = []
        limits[broken[1]].append(broken[7])

order = ""
next = []

for step in steps:
    found = False
    for key in limits:
        # print(step, limits[key])
        if step in limits[key]:
            found = True
            break
    if not found:
        next.append(step)

while len(limits) > 0:
    print(limits)
    next = sorted(next)
    print(next)
    newNext = []
    for item in next:
        newNext.extend(limits.pop(item, []))
        order += item
    next = newNext.copy()

print(order)