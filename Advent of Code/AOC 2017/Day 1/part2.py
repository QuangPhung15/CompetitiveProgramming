with open("input.txt") as file:
    data = file.read()
    nums = data

res = 0
n = len(nums)

for i in range(n):
    if (nums[i] == nums[(i + n // 2) % n]):
        res += int(nums[i])

print(res)
