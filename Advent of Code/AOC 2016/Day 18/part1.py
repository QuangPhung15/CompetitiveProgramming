with open("input.txt") as file:
    data = file.read()
    dp = data

res = dp.count(".")
n = len(dp)
rows = 40

def helper(i):
    count = 0

    for j in range(-1, 2):
        if (0 <= i + j < n and dp[i + j] == "^"):
            count += 1
    
    return True if ((count == 1 and dp[i] == ".") or (count == 2 and dp[i] == "^")) else False

for _ in range(rows - 1):
    curr = ""

    for i in range(n):
        if (helper(i)):
            curr += "^"
        else:
            curr += "."
            res += 1
    
    dp = curr

print(res)
