with open("input.txt") as file:
    data = file.read()
    depth = list(map(int, data.splitlines()))

res = 0
l, curr = 0, 0

for r, d in enumerate(depth):
    curr += d
    
    if (r - l + 1 == 4):
        if (curr - depth[l] > curr - d):
            res += 1
        
        curr -= depth[l]
        l += 1

print(res)
