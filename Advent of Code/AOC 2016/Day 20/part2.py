with open("input.txt") as file:
    data = file.read().splitlines()
    ips = []

    for d in data:
        line = tuple(map(int, d.split("-")))
        ips.append(line)

res = 0
ips.sort(key = lambda x: x[0])
left, right = -1, -1

for l, r in ips:
    if (l <= right):
        right = max(right, r)
    else:
        res += l - right - 1
        left, right = l, r
    
res += 4294967295 - right
print(res)
