with open("input.txt") as file:
    data = file.read()
    offsets = list(map(int, data.splitlines()))

res = 0
n = len(offsets)
i = 0

while (0 <= i < n):
    steps = offsets[i]

    if (steps >= 3):
        offsets[i] -= 1
    else:
        offsets[i] += 1
        
    i += steps
    res += 1

print(res)
