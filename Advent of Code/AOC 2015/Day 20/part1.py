with open("input.txt") as file:
    data = file.read()
    presents = int(data)

target = presents // 10
houses = [0] * (target + 1)

for i in range(1, target + 1):
    for j in range(i, target + 1, i):
        houses[j] += i

res = next(
    i for i in range(1, target + 1) if (houses[i] >= target)
)
print(res)
