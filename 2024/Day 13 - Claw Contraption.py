'''
# Part 1

import re

buttonAs = []
buttonBs = []
prizes = []

with open('2024/data/day13.txt') as file:
    for line in file:
        if line[:8] == "Button A":
            nums = re.findall(r'\d+', line.strip())
            buttonAs.append(tuple(int(num) for num in nums))
        elif line[:8] == "Button B":
            nums = re.findall(r'\d+', line.strip())
            buttonBs.append(tuple(int(num) for num in nums))
        elif line[:5] == "Prize":
            nums = re.findall(r'\d+', line.strip())
            prizes.append(tuple(int(num) for num in nums))

cost = 0

for pos, goal in enumerate(prizes):
    prices = []
    for i in range(101):
        for j in range(101):
            testx = buttonAs[pos][0] * i + buttonBs[pos][0] * j
            testy = buttonAs[pos][1] * i + buttonBs[pos][1] * j
            if testx == goal[0] and testy == goal[1]:
                prices.append(i * 3 + j)
    if len(prices) > 0:
        cost += min(prices)

print(cost)
'''

# Part 2

import re

buttonAs = []
buttonBs = []
prizes = []

with open('2024/data/day13.txt') as file:
    for line in file:
        if line[:8] == "Button A":
            nums = re.findall('\d+', line.strip())
            buttonAs.append(tuple(int(num) for num in nums))
        elif line[:8] == "Button B":
            nums = re.findall('\d+', line.strip())
            buttonBs.append(tuple(int(num) for num in nums))
        elif line[:5] == "Prize":
            nums = re.findall('\d+', line.strip())
            prizes.append(tuple(int(num) for num in nums))

cost = 0

for pos, goal in enumerate(prizes):
    goal = (10000000000000 + goal[0], 10000000000000 + goal[1])
    a0, a1 = buttonAs[pos]
    b0, b1 = buttonBs[pos]
    aX = round((goal[1] - ((b1 * goal[0]) / b0)) / (a1 - ((b1 * a0) / b0)))
    bX = round((goal[0] - (aX * a0)) / b0)
    if aX * a0 + bX * b0 == goal[0] and aX * a1 + bX * b1 == goal[1]:
        cost += aX * 3 + bX

print(cost)