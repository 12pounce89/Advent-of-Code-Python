'''
# Part 1

ids = []

with open('2018/data/day2.txt') as file:
    for line in file:
        ids.append(list(line.strip()))

doubles = 0
triples = 0

for id in ids:
    chars = {}
    for letter in id:
        if letter not in chars:
            chars[letter] = 0
        chars[letter] += 1
    for key in chars:
        if chars[key] == 2:
            doubles += 1
            break
    for key in chars:
        if chars[key] == 3:
            triples += 1
            break

print(doubles * triples)
'''

# Part 2

ids = []

with open('2018/data/day2.txt') as file:
    for line in file:
        ids.append(list(line.strip()))

found = False

for i, id1 in enumerate(ids):
    for j in range(i + 1, len(ids)):
        id2 = ids[j]
        for k in range(len(id1)):
            val1 = id1.pop(k)
            val2 = id2.pop(k)
            if id1 == id2:
                found = True
                break
            id1.insert(k, val1)
            id2.insert(k, val2)
        if found:
            break
    if found:
        break

print("".join(id1))