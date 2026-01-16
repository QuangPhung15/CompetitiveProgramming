with open("input.txt") as file:
    data = file.read()
    banks = list(map(int, data.split()))

res = 0
n = len(banks)
visited = set()

while (tuple(banks) not in visited):
    visited.add(tuple(banks))
    target = max(banks)
    k = banks.index(target)
    banks[k] = 0
    d, r = target // n, target % n

    for _ in range(n):
        k = (k + 1) % n
        banks[k] += d + min(1, r)
        r = max(0, r - 1)

    res += 1

print(res)