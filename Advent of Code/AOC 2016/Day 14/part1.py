from hashlib import md5
from collections import defaultdict, deque

with open("input.txt") as file:
    data = file.read()
    salt = data

q = deque()
count = defaultdict(int)
mapping = {}
curr = -1
keys = 0

def find_hash(n):
    input_str = salt + str(n)
    hash = md5(input_str.encode("utf-8")).hexdigest()
    return hash

def three_of_a_kind(hash):
    for i in range(len(hash) - 2):
        if (hash[i] == hash[i + 1] == hash[i + 2]):
            return hash[i]
    
    return ""

def five_of_a_kind(hash):
    fives = set()

    for i in range(len(hash) - 4):
        if (hash[i] == hash[i + 1] == hash[i + 2] == hash[i + 3] == hash[i + 4]):
            fives.add(hash[i])
    
    return fives

for _ in range(1000):
    curr += 1
    hash = find_hash(curr)
    fives = five_of_a_kind(hash)
    mapping[curr] = fives

    for f in fives:
        count[f] += 1
    
    q.append(hash)

while (keys < 64):
    curr += 1
    hash = find_hash(curr)
    fives = five_of_a_kind(hash)
    mapping[curr] = fives

    for f in fives:
        count[f] += 1
    
    q.append(hash)

    for m in mapping[curr - 1000]:
        count[m] -= 1

    hash = q.popleft()
    three = three_of_a_kind(hash)

    if (three and count[three] > 0):
        keys += 1
    
res = curr - 1000
print(res)
