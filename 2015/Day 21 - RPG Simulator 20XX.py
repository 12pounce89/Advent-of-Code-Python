'''
# Part 1

boss = []

with open('2015/data/day21.txt') as file:
    for line in file:
        boss.append(int(line.strip().split(": ")[1]))

weapons = [(4, 8), (5, 10), (6, 25), (7, 40), (8, 74)]
armors = [(0, 0), (1, 13), (2, 31), (3, 53), (4, 72), (5, 102)]
rings = [(0, 0, 0), (1, 0, 25), (2, 0, 50), (3, 0, 100), (0, 1, 20), (0, 2, 40), (0, 3, 80)]
combos = []

for weapon in weapons:
    for armor in armors:
        for ring1 in rings:
            for ring2 in rings:
                price = weapon[1] + armor[1] + ring1[2]
                damage = weapon[0] + ring1[0]
                defense = armor[0] + ring1[1]
                if ring1 != ring2 or rings.index(ring1) == 0:
                    price += ring2[2]
                    damage += ring2[0]
                    defense += ring2[1]
                combos.append([damage, defense, price])

winning = []

for combo in combos:
    myHealth = 100
    bossHealth = boss[0]
    if combo[0] - boss[2] > 0:
        myAttack = combo[0] - boss[2]
    else:
        myAttack = 1
    if boss[1] - combo[1] > 0:
        bossAttack = boss[1] - combo[1]
    else:
        bossAttack = 1
    while True:
        bossHealth -= myAttack
        myHealth -= bossAttack
        if bossHealth <= 0:
            winning.append(combo[2])
            break
        elif myHealth <= 0:
            break

print(min(winning))
'''

# Part 2

boss = []

with open('2015/data/day21.txt') as file:
    for line in file:
        boss.append(int(line.strip().split(": ")[1]))

weapons = [(4, 8), (5, 10), (6, 25), (7, 40), (8, 74)]
armors = [(0, 0), (1, 13), (2, 31), (3, 53), (4, 72), (5, 102)]
rings = [(0, 0, 0), (1, 0, 25), (2, 0, 50), (3, 0, 100), (0, 1, 20), (0, 2, 40), (0, 3, 80)]
combos = []

for weapon in weapons:
    for armor in armors:
        for ring1 in rings:
            for ring2 in rings:
                price = weapon[1] + armor[1] + ring1[2]
                damage = weapon[0] + ring1[0]
                defense = armor[0] + ring1[1]
                if ring1 != ring2 or rings.index(ring1) == 0:
                    price += ring2[2]
                    damage += ring2[0]
                    defense += ring2[1]
                combos.append([damage, defense, price])

lost = []

for combo in combos:
    myHealth = 100
    bossHealth = boss[0]
    if combo[0] - boss[2] > 0:
        myAttack = combo[0] - boss[2]
    else:
        myAttack = 1
    if boss[1] - combo[1] > 0:
        bossAttack = boss[1] - combo[1]
    else:
        bossAttack = 1
    while True:
        bossHealth -= myAttack
        myHealth -= bossAttack
        if bossHealth <= 0:
            break
        elif myHealth <= 0:
            lost.append(combo[2])
            break

print(max(lost))