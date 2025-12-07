with open("input.txt") as file:
    data = file.read().splitlines()
    banks = data

res = 0

for b in banks:
    first, second = 0, 0

    for i, c in enumerate(b):
        if (i + 1 < len(b) and int(c) > first):
            first = int(b[i])
            second = int(b[i + 1])
        else:
            second = max(second, int(b[i]))

    res += first * 10 + second

print(res)
