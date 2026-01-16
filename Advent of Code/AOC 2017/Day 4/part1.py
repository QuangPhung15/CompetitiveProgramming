with open("input.txt") as file:
    data = file.read().splitlines()
    passphrases = [d.split() for d in data]

res = 0

for passphrase in passphrases:
    seen = set()
    res += 1

    for p in passphrase:
        if (p in seen):
            res -= 1
            break

        seen.add(p)

print(res)    
