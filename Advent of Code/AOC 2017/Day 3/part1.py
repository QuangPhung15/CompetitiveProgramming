with open("input.txt") as file:
    data = file.read()
    location = int(data)

res = -1
r, c = 0, 0
dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
dimensions = [1, 1]
curr = 1

while (curr < location):
    for i, (dr, dc) in enumerate(dirs):
        n = dimensions[i % 2]

        for _ in range(n):
            curr += 1
            r, c = r + dr, c + dc

            if (curr == location):
                res = abs(r) + abs(c)
                break
        
        if (res != -1):
            break
    
        dimensions[i % 2] += 1

print(res)