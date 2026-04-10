with open("input.txt") as file:
    data = file.read().splitlines()
    stats = []

    for d in data:
        line = d.split()
        stats.append((int(line[3]), int(line[6]), int(line[13])))

res = 0
seconds = 2503

for speed, duration, rest in stats:
    time = duration + rest
    d, r = seconds // time, seconds % time
    res = max(res, speed * (d * duration + min(duration, r)))

print(res)
