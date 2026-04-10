from collections import deque
from itertools import combinations

with open("input1.txt") as file:
    data = file.read().splitlines()
    mapping = {}
    chips, generators = [], []
    index = 0

    for i, d in enumerate(data):
        line = d.split()

        for j in range(len(line) - 1):
            if ("generator" in line[j + 1]):
                if (line[j] not in mapping):
                    mapping[line[j]] = index
                    index += 1
                    chips.append(-1)
                    generators.append(-1)
                
                generators[mapping[line[j]]] = i + 1
            if ("microchip" in line[j + 1]):
                if (line[j][:-11] not in mapping):
                    mapping[line[j][:-11]] = index
                    index += 1
                    chips.append(-1)
                    generators.append(-1)
                
                chips[mapping[line[j][:-11]]] = i + 1

def is_safe(chips, gens):
    for floor in range(1, 5):
        count = 0
        
        for g in gens:
            if (g == floor):
                count += 1
        
        if (count == 0):
            continue
            
        for c, g in zip(chips, gens):
            if (c == floor and g != c):
                return False
    
    return True

def canonical_state(elevator, chips, gens):
    pairs = tuple(sorted(zip(chips, gens)))
    return (elevator, pairs)

res = -1
n = len(chips)
start = canonical_state(1, chips, generators)
q = deque([(start, 0)])
visited = set([start])

while (q):
    (elevator, pairs), steps = q.popleft()
    chips = [c for c, _ in pairs]
    gens = [g for _, g in pairs]

    if (all(c == 4 and g == 4 for c, g in zip(chips, gens))):
        res = steps
        break

    items = []

    for i in range(n):
        if (chips[i] == elevator):
            items.append(("C", i))

        if (gens[i] == elevator):
            items.append(("G", i))

    for count in [1, 2]:
        for move_items in combinations(items, count):
            for direction in [-1, 1]:
                new_floor = elevator + direction

                if (new_floor < 1 or new_floor > 4):
                    continue

                if (direction == -1):
                    if (all(c >= elevator and g >= elevator for c, g in pairs)):
                        continue

                new_chips = chips.copy()
                new_gens = gens.copy()

                for kind, i in move_items:
                    if (kind == "C"):
                        new_chips[i] = new_floor
                    else:
                        new_gens[i] = new_floor

                if (not is_safe(new_chips, new_gens)):
                    continue

                new_state = canonical_state(new_floor, new_chips, new_gens)

                if (new_state not in visited):
                    visited.add(new_state)
                    q.append((new_state, steps + 1))

print(res)
