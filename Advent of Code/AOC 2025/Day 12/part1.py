with open("input.txt") as file:
    data = file.read()
    parts = data.split("\n\n")
    presents = []
    regions = []

    for p in parts[:-1]:
        present = p.splitlines()    
        presents.append(present[1:])
    
    for p in parts[-1].splitlines():
        size, count = p.split(": ")
        regions.append((tuple(map(int, size.split("x"))), tuple(map(int, count.split()))))

res = 0

for (w, l), count in regions:    
    if ((w // 3) * (l // 3) >= sum(count)):
        res += 1

print(res)
