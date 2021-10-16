#Uses python3
#[Обход в ширину](https://neerc.ifmo.ru/wiki/index.php?title=%D0%9E%D0%B1%D1%85%D0%BE%D0%B4_%D0%B2_%D1%88%D0%B8%D1%80%D0%B8%D0%BD%D1%83)
import sys
import queue

def bfs(adj, s, t):
    d = [0] * len(adj)
    #d[s] = 0
    Q = queue.Queue()
    Q.put(s)
    while Q.empty() == False:
        if d[t] != 0:
            #print("test")
            return d[t] 
        u = Q.get()
        for j in adj[u]:
            if d[j] == 0:
                Q.put(j)
                d[j] = d[u] + 1
                    
    return d[t]


def distance(adj, s, t):
    ans = bfs(adj,s,t)
    if ans == 0:
        return -1
    else:
        return ans

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
