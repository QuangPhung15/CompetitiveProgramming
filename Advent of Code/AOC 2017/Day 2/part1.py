with open("input.txt") as file:
    data = file.read().splitlines()
    spreadsheet = [list(map(int, d.split())) for d in data]

res = 0

for s in spreadsheet:
    mn, mx = min(s), max(s)
    res += mx - mn

print(res)
