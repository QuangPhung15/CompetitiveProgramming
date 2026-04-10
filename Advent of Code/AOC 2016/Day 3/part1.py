with open("input.txt") as file:
    data = file.read().splitlines()
    triangles = [tuple(map(int, d.split())) for d in data]

res = 0

for a, b, c in triangles:
    longest = max(a, b, c)
    remaining = a + b + c - longest

    if (remaining > longest):
        res += 1

print(res)
