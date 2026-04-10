with open("input.txt") as file:
    data = file.read()
    location = int(data)

res = -1
r, c = 0, 0
dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
dimensions = [1, 1]
squares = {(0, 0): 1}

def helper(r, c):
    total = 0

    for dr in range(-1, 2):
        for dc in range(-1, 2):
            newR, newC = r + dr, c + dc

            if ((newR, newC) in squares):
                total += squares[(newR, newC)]
    
    return total

while (res <= location):
    for i, (dr, dc) in enumerate(dirs):
        n = dimensions[i % 2]

        for _ in range(n):
            r, c = r + dr, c + dc
            curr = helper(r, c)

            if (curr > location):
                res = curr
                break
            
            squares[(r, c)] = curr
        
        if (res != -1):
            break
    
        dimensions[i % 2] += 1

print(res)