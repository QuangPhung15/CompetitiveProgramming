import collections

with open("input.txt") as file:
    data = file.read().split("\n\n")
    medicine = data[1]
    replacements = collections.defaultdict(list)

    for d in data[0].splitlines():
        line = d.split()
        replacements[line[0]].append(line[2])

n = len(medicine)
seen = set()

for i in range(n):
    if (medicine[i] in replacements):
        for r in replacements[medicine[i]]:
            new_med = medicine[:i] + r + medicine[i + 1:]
            seen.add(new_med)
    
    if (i + 1 < n and medicine[i:i + 2] in replacements):
        for r in replacements[medicine[i:i + 2]]:
            new_med = medicine[:i] + r + medicine[i + 2:]
            seen.add(new_med)

res = len(seen)
print(res)
