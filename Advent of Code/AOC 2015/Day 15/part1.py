with open("input.txt") as file:
    data = file.read().splitlines()
    ingredients = []

    for d in data:
        line = d.split()
        ingredients.append((int(line[2][:-1]), int(line[4][:-1]), int(line[6][:-1]), int(line[8][:-1]), int(line[10])))
    
res = 0
n = len(ingredients)
amount = [0] * n

def helper():
    if (sum(amount) < 100):
        return 0
    
    total = 1

    for j in range(4):
        curr = 0

        for i in range(n):
            curr += ingredients[i][j] * amount[i]
        
        total *= max(0, curr)
    
    return total

def backtrack(i, count):
    global res

    if (i == n):
        res = max(res, helper())
        return 

    for k in range(count + 1):
        amount[i] = k
        backtrack(i + 1, count - k)
        amount[i] = 0

backtrack(0, 100)
print(res)
