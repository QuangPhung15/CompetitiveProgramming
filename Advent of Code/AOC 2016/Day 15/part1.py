with open("input1.txt") as file:
    data = file.read().splitlines()
    discs = []

    for d in data:
        line = d.split()
        discs.append((int(line[3]), int(line[-1][:-1])))

res = -1
n = len(discs)
curr = 0

while (True):
    count = 0

    for i in range(n):
        time = curr + i + 1
        pos = (time + discs[i][1]) % discs[i][0]

        if (pos == 0):
            count += 1
    
    if (count == n):
        res = curr
        break

    curr += 1

print(res)
