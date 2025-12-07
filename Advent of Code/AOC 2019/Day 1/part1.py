with open("input.txt") as file:
    data = file.read()
    mass = list(map(int, data.splitlines()))

res = 0

for m in mass:
    res += (m // 3) - 2

print(res)
