with open("input.txt") as file:
    data = file.read().splitlines()
    passphrases = [d.split() for d in data]

res = 0

def helper(word):
    count = [0] * 26

    for w in word:
        count[ord(w) - ord("a")] += 1

    return tuple(count)

for passphrase in passphrases:
    seen = set()
    res += 1

    for p in passphrase:
        count = helper(p)

        if (count in seen):
            res -= 1
            break

        seen.add(count)

print(res)    
