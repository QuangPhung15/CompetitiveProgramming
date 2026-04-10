with open("input.txt") as file:
    data = file.read().splitlines()
    positions = [list(map(int, d.split(","))) for d in data]

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, n):
        p = self.par[n]

        while (p != self.par[p]):
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        
        return p

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if (p1 == p2):
            return False

        if (self.rank[p1] > self.rank[p2]):
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
            return self.rank[p1] == len(self.rank)
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
            return self.rank[p2] == len(self.rank)

def helper(pos1, pos2):
    return pow((pos1[0] - pos2[0]), 2) + pow((pos1[1] - pos2[1]), 2) + pow((pos1[2] - pos2[2]), 2)

n = len(positions)
uf = UnionFind(n)
dist = []

for i in range(n - 1):
    for j in range(i + 1, n):        
        curr = helper(positions[i], positions[j])
        dist.append((curr, i, j))

dist.sort(key = lambda x: x[0])

for _, n1, n2 in dist:
    if (uf.union(n1, n2)):
        res = positions[n1][0] * positions[n2][0]
        break

print(res)
