with open("input.txt") as file:
    data = file.read().splitlines()
    ips = []

    for d in data:
        line = tuple(map(int, d.split("-")))
        ips.append(line)

res = 0
ips.sort(key = lambda x: x[0])

for l, r in ips:
    if (l <= res <= r):
        res = r + 1

print(res)
