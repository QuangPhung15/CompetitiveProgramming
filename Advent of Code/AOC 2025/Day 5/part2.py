with open("input.txt") as file:
    data = file.read().splitlines()
    i = data.index("")
    a, b = data[:i], data[i + 1:]

ranges = [tuple(map(int, r.split("-"))) for r in a]
ids = list(map(int, b))

res = 0
ranges.sort(key = lambda x: x[0])
left, right = ranges[0]

for l, r in ranges:
    if (l <= right):
        right = max(right, r)
    else:
        res += right - left + 1
        left, right = l, r

res += right - left + 1

print(res)
