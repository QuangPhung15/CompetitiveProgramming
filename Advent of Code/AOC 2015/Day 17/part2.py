with open("input.txt") as file:
    data = file.read()
    containers = list(map(int, data.splitlines()))

res = 0
mn = float("inf")
n = len(containers)

def backtrack(i, curr, count):
    global res, mn

    if (i == n):
        if (curr != 0):
            return

        if (count < mn):
            mn = count
            res = 1
        elif (count == mn):
            res += 1
        
        return

    backtrack(i + 1, curr, count)
    backtrack(i + 1, curr - containers[i], count + 1)

backtrack(0, 150, 0)
print(res)
