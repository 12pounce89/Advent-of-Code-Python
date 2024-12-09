# Part 1

import re

ingredients = []

with open('2015/data/day15.txt') as file:
    for line in file:
        ingredients.append(re.findall('[-+]?\d+', line.strip()))

for i in range(len(ingredients)):
    for j in range(len(ingredients[0])):
        ingredients[i][j] = int(ingredients[i][j])

greatest = 0

for i in range(101):
    for j in range(101 - i):
        for k in range(101 - i - j):
            for l in range(101 - i - j - k):
                frosting = ingredients[0][0] * i + ingredients[1][0] * j + ingredients[2][0] * k + ingredients[3][0] * l
                candy = ingredients[0][1] * i + ingredients[1][1] * j + ingredients[2][1] * k + ingredients[3][1] * l
                butterscotch = ingredients[0][2] * i + ingredients[1][2] * j + ingredients[2][2] * k + ingredients[3][2] * l
                sugar = ingredients[0][3] * i + ingredients[1][3] * j + ingredients[2][3] * k + ingredients[3][3] * l
                calories = ingredients[0][4] * i + ingredients[1][4] * j + ingredients[2][4] * k + ingredients[3][4] * l
                if calories == 500:
                    mult = frosting * candy * butterscotch * sugar
                    if frosting < 0 or candy < 0 or butterscotch < 0 or sugar < 0:
                        mult = 0
                    if mult > greatest:
                        greatest = mult

print(greatest)