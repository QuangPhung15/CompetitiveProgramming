with open("input.txt") as file:
    data = file.read().splitlines()

nums = []

for d in data[:-1]:
    nums.append(list(map(int, d.split())))

ops = data[-1].split()

res = 0

for i, o in enumerate(ops):
    if (o == "+"):
        curr = 0

        for num in nums:
            curr += num[i]
    else:
        curr = 1

        for num in nums:
            curr *= num[i]
    
    res += curr

print(res)
