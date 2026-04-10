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

mx1, mx2, mx3 = 0, 0, 0

for c in calories:
    calo = sum(c)

    if (calo > mx1):
        mx3 = mx2
        mx2 = mx1
        mx1 = calo
    elif (calo > mx2):
        mx3 = mx2
        mx2 = calo
    elif (calo > mx3):
        mx3 = calo

res = mx1 + mx2 + mx3

print(res)
