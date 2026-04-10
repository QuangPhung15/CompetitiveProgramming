import collections

with open("input.txt") as file:
    data = file.read().splitlines()
    rooms = []

    for d in data:
        line = d.split("-")
        names = line[:-1]
        sector_id, checksum = line[-1].split("[")
        rooms.append((names, int(sector_id), checksum[:-1]))

res = 0

for names, sector_id, checksum in rooms:
    count = collections.defaultdict(int)

    for name in names:
        for n in name:
            count[n] += 1
    
    sorted_count = sorted(list(count.items()), key = lambda x: (-x[1], x[0]))

    if (len(sorted_count) < len(checksum)):
        continue

    res += sector_id

    for i in range(len(checksum)):
        if (checksum[i] != sorted_count[i][0]):
            res -= sector_id
            break

print(res)
