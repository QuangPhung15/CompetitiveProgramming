from collections import deque

with open("input.txt") as file:
    data = file.read()
    n = int(data)

elves1 = deque([i for i in range(1, n // 2 + 1)])
elves2 = deque([i for i in range(n // 2 + 1, n + 1)])

while (elves1 and elves2):
    elves2.popleft()
    elves2.append(elves1.popleft())

    if (len(elves1) + 1 < len(elves2)):
        elves1.append(elves2.popleft())
    
res = elves1[0] if (elves1) else elves2[0]
print(res)
