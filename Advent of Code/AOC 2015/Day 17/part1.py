with open("input.txt") as file:
    data = file.read()
    containers = list(map(int, data.splitlines()))

n = len(containers)

def backtrack(i, curr):
    if (i == n):
        return 1 if (curr == 0) else 0
    
    return backtrack(i + 1, curr) + backtrack(i + 1, curr - containers[i])

res = backtrack(0, 150)
print(res)
