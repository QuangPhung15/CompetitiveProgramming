with open("input.txt") as file:
    data = file.read()
    banks = list(map(int, data.split()))

index = 0
n = len(banks)
visited = {}

while (tuple(banks) not in visited):
    visited[tuple(banks)] = index
    target = max(banks)
    k = banks.index(target)
    banks[k] = 0
    d, r = target // n, target % n

    for _ in range(n):
        k = (k + 1) % n
        banks[k] += d + min(1, r)
        r = max(0, r - 1)

    index += 1

res = index - visited[tuple(banks)]
print(res)