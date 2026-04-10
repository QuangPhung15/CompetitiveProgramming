import collections

with open("input.txt") as file:
    data = file.read().split("\n\n")
    medicine = data[1]
    replacements = collections.defaultdict(list)

    for d in data[0].splitlines():
        line = d.split()
        replacements[line[0]].append(line[2])

def bfs(medicine):
    steps = 0

    while (medicine != "e"):
        for src, dsts in replacements.items():
            for dst in dsts:
                if (dst in medicine):
                    medicine = medicine.replace(dst, src, 1)
                    steps += 1
                    break
     
    return steps

res = bfs(medicine)
print(res)
