with open("input.txt") as file:
    data = file.read().splitlines()
    calories = []
    curr = []

    for d in data:
        if (d != ""):
            curr.append(int(d))
        else:
            calories.append(curr)
            curr = []
    
    calories.append(curr)

res = 0

for c in calories:
    res = max(res, sum(c))

print(res)
