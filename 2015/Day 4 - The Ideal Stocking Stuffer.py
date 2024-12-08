# Part 1

import hashlib
key = ""

with open('2015/data/day4.txt') as file:
    for line in file:
        key += line.strip()

hashed = hashlib.md5(key.encode())
num = 0

while hashed.hexdigest()[:6] != "000000":
    num += 1
    testKey = key + str(num)
    hashed = hashlib.md5(testKey.encode())

print(num)