with open("input.txt") as file:
    data = file.read().splitlines()
    adj = {}

    for d in data:
        src, dst = d.split(":")
        adj[src] = dst.split()

visited = {}

def dfs(curr):
    if (curr == "out"):
        return 1
    
    if (curr not in visited):
        res = 0

        for a in adj[curr]:
            res += dfs(a)
        
        visited[curr] = res
    
    return visited[curr]

res = dfs("you")

print(res)
