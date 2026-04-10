with open("input.txt") as file:
    data = file.read().splitlines()
    ranges = data[0].split(",")

res = 0

for r in ranges:
    s, e = map(int, r.split("-"))

    for i in range(s, e + 1):
        num = str(i)
        nums = num * 2
        n = len(nums)

        if (num in nums[1:n - 1]):
            res += i

print(res)
