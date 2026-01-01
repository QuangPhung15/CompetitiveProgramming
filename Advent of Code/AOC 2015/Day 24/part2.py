with open("input.txt") as file:
    data = file.read()
    weights = list(map(int, data.splitlines()))

res = -1
size = float("inf")
n = len(weights)
target = sum(weights) // 4
weights.sort(reverse=True)

def backtrack(i, total, prod, count):
    global res, size

    if (total > target or count > size):
        return

    if (i == n):
        if (total == target):
            if (count < size or (count == size and prod < res)):
                res = prod
                size = count
                
        return

    backtrack(i + 1, total, prod, count)
    backtrack(i + 1, total + weights[i], prod * weights[i], count + 1)

backtrack(0, 0, 1, 0)
print(res)
