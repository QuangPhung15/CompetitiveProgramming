with open("input.txt") as file:
    data = file.read().splitlines()
    i = data.index("")
    a, b = data[:i], data[i + 1:]

ranges = [tuple(map(int, r.split("-"))) for r in a]
ids = list(map(int, b))

res = 0

for i in ids:
    for l, r in ranges:
        if (l <= i <= r):
            res += 1
            break

print(res)
