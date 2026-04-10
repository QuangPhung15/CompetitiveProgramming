with open("input.txt") as file:
    data = file.read().splitlines()
    dimensions = [list(map(int, d.split("x"))) for d in data]

res = 0

for l, w, h in dimensions:
    a1, a2, a3 = l * w, w * h, l * h
    extra = min(a1, a2, a3)
    res += 2 * (a1 + a2 + a3) + extra

print(res)
