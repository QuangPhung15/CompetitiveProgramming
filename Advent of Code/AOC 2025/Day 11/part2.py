with open("input.txt") as file:
    data = file.read().splitlines()
    adj = {}

    for d in data:
        src, dst = d.split(":")
        adj[src] = dst.split()

visited = {}

def dfs(curr):
    if (curr == "out"):
        return [1, 0, 0, 0]

    if (curr not in visited):
        res = [0, 0, 0, 0]

        for a in adj[curr]:
            temp = dfs(a)

            if (curr == "fft"):
                res[1] += temp[0]
                res[3] += temp[2]
            elif (curr == "dac"):
                res[2] += temp[0]
                res[3] += temp[2]
            else:
                for i in range(4):
                    res[i] += temp[i]
        
        visited[curr] = res
    
    return visited[curr]

res = dfs("svr")[3]

print(res)
