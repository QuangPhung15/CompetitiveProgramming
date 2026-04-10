with open("input.txt") as file:
    data = file.read().splitlines()
    dimensions = [list(map(int, d.split("x"))) for d in data]

res = 0

for l, w, h in dimensions:
    volume = l * w * h
    p1, p2, p3 = 2 * (l + w), 2 * (w + h), 2 * (l + h)
    res += volume + min(p1, p2, p3)

print(res)
