'''
# Part 1

def next_password(password):
    for i in range(len(password) - 1, -1, -1):
        if password[i] == "z":
            password[i] = "a"
        else:
            if password[i] in "hkn":
                password[i] = chr(ord(password[i]) + 2)
            else:
                password[i] = chr(ord(password[i]) + 1)
            break
    return password

def has_pairs(password):
    i = 0
    pairs = set()
    while i < len(password) - 1:
        if password[i] == password[i + 1]:
            pairs.add(password[i])
            i += 1
        i += 1
    return len(pairs) > 1

def has_triple(password):
    for i in range(len(password) - 2):
        if password[i] + password[i + 1] + password[i + 2] in triples:
            return True
    return False

with open('2015/data/day11.txt') as file:
    for line in file:
        password = list(line.strip())

triples = {chr(97 + i) + chr(98 + i) + chr(99 + i) for i in range(24)}

while True:
    password = next_password(password)
    if not has_triple(password):
        continue
    if not has_pairs(password):
        continue
    break

print("".join(password))
'''

# Part 2

def next_password(password):
    for i in range(len(password) - 1, -1, -1):
        if password[i] == "z":
            password[i] = "a"
        else:
            if password[i] in "hkn":
                password[i] = chr(ord(password[i]) + 2)
            else:
                password[i] = chr(ord(password[i]) + 1)
            break
    return password

def has_pairs(password):
    i = 0
    pairs = set()
    while i < len(password) - 1:
        if password[i] == password[i + 1]:
            pairs.add(password[i])
            i += 1
        i += 1
    return len(pairs) > 1

def has_triple(password):
    for i in range(len(password) - 2):
        if password[i] + password[i + 1] + password[i + 2] in triples:
            return True
    return False

with open('2015/data/day11.txt') as file:
    for line in file:
        password = list(line.strip())

triples = {chr(97 + i) + chr(98 + i) + chr(99 + i) for i in range(24)}

while True:
    password = next_password(password)
    if not has_triple(password):
        continue
    if not has_pairs(password):
        continue
    break

print("".join(password))