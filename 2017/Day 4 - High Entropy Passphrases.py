'''
# Part 1

passphrases = []

with open('2017/data/day4.txt') as file:
    for line in file:
        passphrases.append(line.strip().split())

valid = 0

for passphrase in passphrases:
    setted = set()
    for word in passphrase:
        oldLen = len(setted)
        setted.add(word)
        if oldLen == len(setted):
            break
    if len(setted) == len(passphrase):
        valid += 1

print(valid)
'''

# Part 2

passphrases = []

with open('2017/data/day4.txt') as file:
    for line in file:
        passphrases.append(line.strip().split())

valid = 0

for passphrase in passphrases:
    setted = set()
    for word in passphrase:
        oldLen = len(setted)
        setted.add("".join(sorted(word)))
        if oldLen == len(setted):
            break
    if len(setted) == len(passphrase):
        valid += 1

print(valid)