import collections

with open("input.txt") as file:
    data = file.read()
    messages = data.splitlines()

res = ""
m, n = len(messages), len(messages[0])

for j in range(n):
    count = collections.defaultdict(int)
    c, mx = "", 0

    for i in range(m):
        count[messages[i][j]] += 1

        if (count[messages[i][j]] > mx):
            c = messages[i][j]
            mx = count[messages[i][j]]
    
    res += c

print(res)
