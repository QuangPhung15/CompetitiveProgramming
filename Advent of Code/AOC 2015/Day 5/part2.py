with open("input.txt") as file:
    data = file.read()
    strings = data.splitlines()

res = 0

for s in strings:
    n = len(s)
    has_pair = False
    has_sandwich = False
    seen = {}

    for i in range(n - 1):
        if (i + 2 < n and s[i] == s[i + 2]):
            has_sandwich = True
        
        pair = s[i:i + 2]

        if (pair in seen and seen[pair] + 1 < i):
            has_pair = True
        
        seen[pair] = i
    
    res += has_pair and has_sandwich

print(res)
