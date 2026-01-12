from collections import deque

with open("input.txt") as file:
    data = file.read()
    n = int(data)

elves = deque([i for i in range(1, n + 1)])

while (len(elves) > 1):
    curr = elves.popleft()
    elves.popleft()
    elves.append(curr)

res = elves[0]
print(res)
