with open("input.txt") as file:
    data = file.read()
    report = list(map(int, data.splitlines()))

res = 0
seen = set()

for r in report:
    target = 2020 - r

    if (target in seen):
        res += target * r
    
    seen.add(r)

print(res)
