with open("input.txt") as file:
    data = file.read().splitlines()

nums = []
ops = data[-1]

l = 0

while (l < len(ops)):
    r = l + 1

    while (r < len(ops) and ops[r] == " "):
        r += 1

    if (r < len(ops)):
        r -= 1

    num = []

    for i in range(l, r):
        curr = 0

        for j in range(len(data) - 1):
            if (data[j][i] != " "):
                curr = curr * 10 + int(data[j][i])
        
        num.append(curr)
    
    nums.append(num)
    l = r + 1

ops = ops.split()

res = 0

for i, o in enumerate(ops):
    if (o == "+"):
        curr = 0

        for n in nums[i]:
            curr += n
    else:
        curr = 1

        for n in nums[i]:
            curr *= n
    
    res += curr

print(res)
