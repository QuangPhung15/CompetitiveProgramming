with open("input.txt") as file:
    data = file.read().splitlines()
    stats = []

    for d in data:
        line = d.split()
        stats.append((int(line[3]), int(line[6]), int(line[13])))

seconds = 2503
n = len(stats)
points = [0] * n
reindeers = [[d, r] for _, d, r in stats]
position = [0] * n

for _ in range(seconds):
    for i, (d, r) in enumerate(reindeers):
        if (d > 0):
            position[i] += stats[i][0]
            reindeers[i][0] -= 1

            if (reindeers[i][0] == 0):
                reindeers[i][1] = stats[i][2]
        else:
            reindeers[i][1] -= 1

            if (reindeers[i][1] == 0):
                reindeers[i][0] = stats[i][1]
        
    mx = -1

    for p in position:
        mx = max(mx, p)

    for i in range(n):
        if (position[i] == mx):
            points[i] += 1

res = max(points)
print(res)
