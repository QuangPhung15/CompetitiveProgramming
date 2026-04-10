import collections

with open("input.txt") as file:
    data = file.read()
    messages = data.splitlines()

res = ""
m, n = len(messages), len(messages[0])

for j in range(n):
    count = collections.defaultdict(int)
    c, mn = "", float("inf")

    for i in range(m):
        count[messages[i][j]] += 1
    
    for k, v in count.items():
        if (v < mn):
            mn = v
            c = k
    
    res += c

print(res)
