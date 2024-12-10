# Part 1

import re

pos = []

with open('2015/data/day25.txt') as file:
    for line in file:
        nums = re.findall('\d+', line.strip())
        for num in nums:
            pos.append(int(num))

place = sum(range(1, (pos[0] + pos[1] - 1))) + (pos[1] - 1)
num = 20151125
print(place)

for _ in range(place):
    num = (num * 252533) % 33554393

print(num)