'''
# Part 1

connections = {}

with open('2024/data/day23.txt') as file:
    for line in file:
        broken = line.strip().split("-")
        if broken[0] not in connections:
            connections[broken[0]] = []
        if broken[1] not in connections:
            connections[broken[1]] = []
        connections[broken[0]].append(broken[1])
        connections[broken[1]].append(broken[0])

triples = []

for key in connections:
    list = connections[key]
    for item in list:
        for item2 in list:
            triple = tuple(sorted([key, item, item2]))
            if triple not in triples:
                if item2 in connections[item]:
                    triples.append(triple)


triples = sorted(triples)
withT = []

for triple in triples:
    if triple[0][0] == 't' or triple[1][0] == 't' or triple[2][0] == 't':
        withT.append(triple)

print(len(withT))
'''

# Part 2

connections = {}

with open('2024/data/day23.txt') as file:
    for line in file:
        broken = line.strip().split("-")
        if broken[0] not in connections:
            connections[broken[0]] = []
        if broken[1] not in connections:
            connections[broken[1]] = []
        connections[broken[0]].append(broken[1])
        connections[broken[1]].append(broken[0])

triples = []
max = []

# key = 'wq'
for key in connections:
# for i in range(1):
    list = connections[key]
    largest = [key]
    if len(list) < len(max):
        continue
    for item in list:
        biggest = [key, item]
        for item2 in list:
            if item2 in connections[item] and item2 in list:
                biggest.append(item2)
        for val in biggest:
            for val2 in biggest:
                if val != val2 and val2 not in connections[val]:
                    biggest = []
        if len(biggest) > len(largest):
            largest = biggest[:]
    if len(largest) > len(max):
        max = largest[:]

print(",".join(sorted(max)))