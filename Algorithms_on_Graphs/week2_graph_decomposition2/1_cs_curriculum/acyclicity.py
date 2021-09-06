#Uses python3
import sys

#write your code here
ia = False
def dfs(adj,x,is_acyclic,used):
    global ia
    if is_acyclic[x] == 1:
        ia = True
    else:
        is_acyclic[x] = 1
    
    if used[x] == 0:    
        used[x] = 1
        for i in adj[x]:
                dfs(adj,i,is_acyclic,used)
    is_acyclic[x] = 0

def acyclic(adj):
    global ia
    is_acyclic  = [0 for i in range(len(adj))]
    ia = False
    used = [0] * len(adj) 
    for i in range(len(adj)):
        if used[i] == 0:
            dfs(adj,i,is_acyclic,used)
    return int(ia)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
