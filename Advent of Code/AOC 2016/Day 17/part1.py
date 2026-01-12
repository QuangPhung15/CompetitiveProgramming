from hashlib import md5
from collections import deque

with open("input.txt") as file:
    data = file.read()
    passcode = data

res = ""
m, n = 4, 4
q = deque([(0, 0, "")])
dirs = [(-1, 0, "U"), (1, 0, "D"), (0, -1, "L"), (0, 1, "R")]

def find_hash(path):
    input_str = passcode + path
    output_str = md5(input_str.encode("utf-8")).hexdigest()
    return output_str[:4]

while (q):
    r, c, path = q.popleft()

    if (r == m - 1 and c == n - 1):
        res = path
        break

    hash = find_hash(path)

    for i, (dr, dc, p) in enumerate(dirs):
        newR, newC = r + dr, c + dc
        
        if (newR < 0 or newR >= m or newC < 0 or newC >= n):
            continue

        if (hash[i] == "a" or hash[i].isdigit()):
            continue

        q.append((newR, newC, path + p))

print(res)
