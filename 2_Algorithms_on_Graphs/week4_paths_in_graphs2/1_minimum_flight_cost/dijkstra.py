#Uses python3
import sys
import queue

def dijkstra_search(adj, cost, s, t):
    dist = [float('inf')] * len(adj)
    dist[s] = 0
    H = queue.PriorityQueue()
    H.put(s)
    while not H.empty():
        u = H.get()
        for v, w in enumerate(adj[u]):
            if dist[v] > dist[u] + cost[u][w]:
                dist[v] = dist[u] + cost[u][w]
                H.put(v)
    return dist[t]

def distance(adj, cost, s, t):
    ans = dijkstra_search(adj,cost,s,t)
    if ans == float('inf'):
        return -1
    else:
        return ans

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))