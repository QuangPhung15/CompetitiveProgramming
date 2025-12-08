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
            return

        if (self.rank[p1] > self.rank[p2]):
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]

def helper(pos1, pos2):
    return pow((pos1[0] - pos2[0]), 2) + pow((pos1[1] - pos2[1]), 2) + pow((pos1[2] - pos2[2]), 2)

k = 1000
n = len(positions)
uf = UnionFind(n)
dist = []

for i in range(n - 1):
    for j in range(i + 1, n):        
        curr = helper(positions[i], positions[j])
        dist.append((curr, i, j))

dist.sort(key = lambda x: x[0])

for i in range(k):
    curr, n1, n2 = dist[i]
    uf.union(n1, n2)

mx1, mx2, mx3 = 0, 0, 0

for r in uf.rank:
    if (r > mx1):
        mx3 = mx2
        mx2 = mx1
        mx1 = r
    elif (r > mx2):
        mx3 = mx2
        mx2 = r
    elif (r > mx3):
        mx3 = r

res = mx1 * mx2 * mx3

print(res)
