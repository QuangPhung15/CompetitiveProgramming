import collections

with open("input.txt") as file:
    data = file.read().splitlines()
    locations = [[], []]

    for d in data:
        a, b = map(int, d.split())
        locations[0].append(a)
        locations[1].append(b)

res = 0
n = len(locations[0])
count = collections.defaultdict(int)

for l in locations[1]:
    count[l] += 1

for l in locations[0]:
    res += l * count[l]

print(res)
