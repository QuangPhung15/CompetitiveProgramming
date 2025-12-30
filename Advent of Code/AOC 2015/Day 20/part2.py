with open("input.txt") as file:
    data = file.read()
    presents = int(data)

target = presents // 11 + 1
houses = [0] * (target + 1)

for i in range(1, target + 1):
    for j in range(i, min(i + i * 50, target + 1), i):
        houses[j] += i

res = next(
    i for i in range(1, target + 1) if (houses[i] >= target)
)
print(res)
