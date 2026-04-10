import math

with open("input.txt") as file:
    data = file.read().splitlines()
    boss = []

    for d in data:
        line = d.split()
        boss.append(int(line[-1]))

with open("items.txt") as file:
    data = file.read().split("\n\n")
    weapons, armors, rings = [], [(0, 0, 0)], [(0, 0, 0), (0, 0, 0)]

    for d in data[0].splitlines()[1:]:
        line = d.split()
        weapons.append((int(line[1]), int(line[2]), int(line[3])))
    
    for d in data[1].splitlines()[1:]:
        line = d.split()
        armors.append((int(line[1]), int(line[2]), int(line[3])))
    
    for d in data[2].splitlines()[1:]:
        line = d.split()
        rings.append((int(line[2]), int(line[3]), int(line[4])))

res = float("inf")
cost = 0
p_damage, p_armor = 0, 0

def helper(d1, a1, d2, a2):
    player_hp, enemy_hp = 100, boss[0]
    p_attack, e_attack = max(1, d1 - a2), max(1, d2 - a1)
    p_rounds, e_rounds = math.ceil(enemy_hp / p_attack), math.ceil(player_hp / e_attack)
    return p_rounds <= e_rounds

for i in range(len(weapons)):
    cost += weapons[i][0]
    p_damage += weapons[i][1]
    
    for j in range(len(armors)):
        cost += armors[j][0]
        p_armor += armors[j][2]

        for k in range(len(rings) - 1):
            for t in range(k + 1, len(rings)):
                cost += rings[k][0] + rings[t][0]
                p_damage += rings[k][1] + rings[t][1]
                p_armor += rings[k][2] + rings[t][2]

                if (helper(p_damage, p_armor, boss[1], boss[2])):
                    res = min(res, cost)

                cost -= rings[k][0] + rings[t][0]
                p_damage -= rings[k][1] + rings[t][1]
                p_armor -= rings[k][2] + rings[t][2]
        
        cost -= armors[j][0]
        p_armor -= armors[j][2]
    
    cost -= weapons[i][0]
    p_damage -= weapons[i][1]

print(res)
