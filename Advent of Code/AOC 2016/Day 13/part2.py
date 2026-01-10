from collections import deque

with open("input.txt") as file:
    data = file.read()
    fav_num = int(data)

def helper(x, y):
    count = 0
    n = x * x + 3 * x + 2 * x * y + y + y * y + fav_num
    
    while (n > 0):
        count += n & 1
        n >>= 1
    
    return count % 2 == 0

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
q = deque([(0, 1, 1)])
visited = set([(1, 1)])

while (q):
    steps, x, y = q.popleft()

    if (steps == 50):
        continue

    for dx, dy in dirs:
        newX, newY = x + dx, y + dy

        if (newX < 0 or newY < 0):
            continue

        if ((newX, newY) in visited):
            continue
        
        if (not helper(newX, newY)):
            continue
            
        q.append((steps + 1, newX, newY))
        visited.add((newX, newY))

res = len(visited)
print(res)
